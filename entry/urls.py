from unicodedata import name
from django.urls import path, include
from entry.views import sgnup, logn, info, logout
urlpatterns = [
    path('register',sgnup.as_view(),name='register'),
    path('fieldinfo',info,name='fdinfo'),
    path('login/',logn,name='login'),
    path('logout/',logout, name='logout')
]