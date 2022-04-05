from cProfile import label
from dataclasses import fields
from pyexpat import model
from turtle import fd
from django import forms
from django.forms import ModelForm 

from .models import fields as fds, Certificates

from .models import usrinfo
class UIform(forms.Form):
    DP=forms.ImageField(label='Profile Picture')
    fdsneeded=forms.ModelMultipleChoiceField(queryset=fds.objects.all(),label='Fields in which you needed guidance')
    fdsexpert=forms.ModelMultipleChoiceField(queryset=fds.objects.all(),label='Fields in which you are expert')
class crtfform(forms.Form):
    class Meta:
        model=Certificates
        fields=['fd','issuedby','certificate']
    
    
    
