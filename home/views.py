from nturl2path import url2pathname
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from entry.models import usrinfo
from django.contrib.auth.models import User



def home(request):
    us=request.user
    usr=User.objects.get(username=str(us))
    if request.method=='POST':
        if 'ch_connectmode' in request.POST:
            if usr.guideinfo.connectmode==0:
                usr.guideinfo.connectmode=1
            elif usr.guideinfo.connectmode==1:
                usr.guideinfo.connectmode=0
            usr.guideinfo.save()
    fdsneeded=usr.guideeinfo.fds.all()
    fdsexpert=usr.guideinfo.fds.all()
    notseengderms = []
    for rm in usr.guideeinfo.guidee_rooms.all():
        for mssg in rm.message_set.all():
            print(mssg.status)
            if mssg.status=="gd1":
                print(rm)
                print(mssg.mssg, mssg.status)
                notseengderms +=[rm]
                break
    
            

    print(notseengderms)        
    return render(request,'home.html',{'fdsneeded':fdsneeded,'fdsexpert':fdsexpert,'notseengderms':notseengderms, 'usr':usr})

