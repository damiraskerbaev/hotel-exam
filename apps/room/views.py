from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect

from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/room_list.html', context=context)
