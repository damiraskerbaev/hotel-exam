from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'damirhotelapi$default',
        'USER': 'damirhotelapi',
        'PASSWORD': 'DaMiR2810',
        'HOST': 'damirhotelapi.mysql.pythonanywhere-services.com'
    }
}