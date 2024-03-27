from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Guest

class SignupForm(UserCreationForm):
    class Meta:
        model = Guest
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email',
            'passport_serie',
        ]


    class LoginForm(AuthenticationForm):
        class Meta:
            model = Guest
            fields = [
                'username',
                'password'
            ]
