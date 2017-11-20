import json
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only
from chat.models import Room


@allowed_hosts_only
@channel_session_user_from_http
def ws_add(message):
    _, room = message['path'].strip('/').split('/')
    user_groups_room = list(message.user.groups.values_list('id', flat=True))
    message.channel_session['room'] = room


    relations_groups_room = list(Room.objects.get(room_slug=room).groups_permissions.values_list('id', flat=True))

    if relations_groups_room:
        l = [p for p in relations_groups_room if p in user_groups_room]
        if not l:
            # Usuários que não estão relacionados com a sala nao podem
            # ler mesangens
            message.reply_channel.send({"accept": False })
            return



    message.reply_channel.send({"accept": True })
    Group(room).add(message.reply_channel)
    Group(room).send({
        "text": json.dumps({
            'username': message.user.username,
            'groups': None,
            'message': "Join!"
        })
    })


@channel_session_user
def ws_message(message):
    data = json.loads(message['text'])
    Group(message.channel_session['room']).send({
        "text": json.dumps({
            'username': message.user.username,
            'groups': list(message.user.groups.values_list('id', flat=True)),
            'message': data['message']
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group(message.channel_session['room']).discard(message.reply_channel)
