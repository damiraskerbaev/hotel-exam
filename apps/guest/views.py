from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Guest
from .serializers import GuestSerielizer
from django.shortcuts import render
from ..booking.models import Booking
from django.urls import reverse_lazy
from .forms import SignupForm
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerielizer

def my_booking(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(guest=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'accounts/account.html', context=context)
    else:
        return render(request, 'accounts/account.html')
    
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('LoginPage')
    context_object_name = 'LoginPage'


def LoginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home_page')