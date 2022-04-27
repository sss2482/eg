from django.contrib import admin
from .models import fields, usrinfo, Question, Review, Rating
admin.site.register(fields)
admin.site.register(usrinfo)
admin.site.register(Question)
admin.site.register(Review)
admin.site.register(Rating)
# Register your models here.
