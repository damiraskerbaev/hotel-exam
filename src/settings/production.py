from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotelexam$default',
        'USER': 'hotelexam',
        'PASSWORD': 'DaMiR2810',
        'HOST': 'hotelexam.mysql.pythonanywhere-services.com'
    }
}