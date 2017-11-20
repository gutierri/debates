import json
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.security.websockets import allowed_hosts_only

@allowed_hosts_only
@channel_session_user_from_http
def ws_add(message):
    user_groups_room = list(message.user.groups.values_list('id', flat=True))
    message.reply_channel.send({"accept": True})
    Group('chat').add(message.reply_channel)
    Group('chat').send({
        "text": json.dumps({
            'username': message.user.username,
            'groups': None,
            'message': "Join!"
        })
    })


@channel_session_user
def ws_message(message):
    data = json.loads(message['text'])
    Group("chat").send({
        "text": json.dumps({
            'username': message.user.username,
            'groups': list(message.user.groups.values_list('id', flat=True)),
            'message': data['message']
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('chat').send({
        "text": json.dumps({
            'username': message.user.username,
            'groups': None,
            'message': "Got out"
        })
    })
    Group("chat").discard(message.reply_channel)
