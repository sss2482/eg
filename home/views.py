from nturl2path import url2pathname
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from entry.models import usrinfo
from django.contrib.auth.models import User
def home(request):
    usr=request.user
    us=User.objects.get(username=str(usr))
    print(us,type(us))
    usinf=usrinfo.objects.get(usr=us)
    fdsneeded=usinf.fdsneeded.all()
    fdsexpert=usinf.fdsexpert.all()
    return render(request,'home.html',{'fdsneeded':fdsneeded,'fdsexpert':fdsexpert})

