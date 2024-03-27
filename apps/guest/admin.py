from django.contrib.admin import *

from .models import Guest

@register(Guest)

class GuestAdmin(ModelAdmin):

    list_display = ('id', 'username')
    list_display_links = ('id', 'username')