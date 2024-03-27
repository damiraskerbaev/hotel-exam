from django.db.models import *
from django.contrib.auth.models import AbstractUser

class Guest(AbstractUser):
    email = EmailField(
        'Email'
    )

    phone_number = CharField(
        'Phone number',
        max_length=13
    )

    passport_serie = CharField(
        'Passport serie',
        max_length=7
    )

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'