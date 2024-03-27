from rest_framework.viewsets import ModelViewSet

from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import render, redirect

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def book_list(request):

    books = Booking.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_list.html', context=context)

def book_detail(request, pk):
    book = Booking.object.get(id=pk)
    context = {'book' : book}
    return render(request, 'book/book_detail.html')