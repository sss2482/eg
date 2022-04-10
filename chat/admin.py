from sys import implementation
import django
from django.contrib import admin

from .models import grp, room, message

admin.site.register(grp)
admin.site.register(room)
admin.site.register(message)