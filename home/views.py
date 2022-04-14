from nturl2path import url2pathname
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from entry.models import usrinfo
from django.contrib.auth.models import User



def home(request):
    usr=request.user
    us=User.objects.get(username=str(usr))
    usinf=usrinfo.objects.get(usr=us)
    if request.method=='POST':
        if 'ch_connectmode' in request.POST:
            if usinf.guide_connectmode==0:
                usinf.guide_connectmode=1
            elif usinf.guide_connectmode==1:
                usinf.guide_connectmode=0
            usinf.save()
    fdsneeded=usinf.fdsneeded.all()
    fdsexpert=usinf.fdsexpert.all()
    notseengderms = []
    for rm in us.usrinfo.guidee_rooms.all():
        for mssg in rm.messages.all():
            if mssg.status=="gd1":
                print(rm)
                print(mssg.mssg, mssg.status)
                notseengderms +=[rm]
                break
    
            

    print(notseengderms)        
    return render(request,'home.html',{'fdsneeded':fdsneeded,'fdsexpert':fdsexpert,'notseengderms':notseengderms, 'usr':usinf})

