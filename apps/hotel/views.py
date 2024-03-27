from rest_framework.viewsets import ModelViewSet

from .models import Hotel
from .serializers import HotelSerializer
from rest_framework.permissions import *
from django.shortcuts import render, redirect



class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

def home_page(request):
    return render(request, 'hotel/home_page.html')

def hotel_list(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/hotel_list.html', context=context)