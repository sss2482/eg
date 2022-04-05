from django.contrib import admin
from .models import fields, usrinfo, Certificates, Question
admin.site.register(fields)
admin.site.register(usrinfo)
admin.site.register(Certificates)
admin.site.register(Question)
# Register your models here.
