from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import ChatRoom


def room_list(request):
    """The 3 (or more) chatroom links, read straight from the database."""
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})


@login_required
def room_detail(request, room_name):
    """
    The actual chat page for one room. Reserved to logged-in users (an
    anonymous visitor is redirected to the Account/login page instead,
    thanks to @login_required + settings.LOGIN_URL).
    """
    room = get_object_or_404(ChatRoom, name=room_name)
    return render(request, 'chat/room_detail.html', {'room': room})
