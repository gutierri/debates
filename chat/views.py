from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def list_rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'chat/list_rooms.html', context)

@login_required
def room(request):
    return render(request, 'chat/room.html')
