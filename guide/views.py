from django.utils import timezone
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime

from entry.models import usrinfo, fields, Question
from chat.models import room


def gde_cntct_lst(request,field):
    fd=fields.objects.get(name=field)
    us=User.objects.get(username=str(request.user))
    usr=usrinfo.objects.get(usr=us)
    questions=[]
    show=request.GET.get('show')
    if show=='chat_gde':
        tp='chat'
        gde_lst=[]
        for rm in usr.guide_rooms.all():
            gde_lst+=[rm.guidee]
        return render(request,'gde_contact_lst.html',{'fd':fd,'gde_lst':gde_lst,'type':tp})
    elif show=='not seen':
        tp='ques'
        shl=[0,]
    elif show=='all':
        tp='ques'
        shl=[1,0]
    if show=='new':
        tp='ques'
        new=True
        for q in usr.questions_byguidees.all():
            print(q.time_asked > usr.guide_lastgdelstseen)
            if q.fd == fd and q.time_asked > usr.guide_lastgdelstseen :
                questions+=[q]
                print(q.guidee.usrinfo.guidee_rating)
        print(questions)
    
    else:
        new=False
        for q in usr.questions_byguidees.all():
            if q.fd == fd and q.status in shl:
                questions+=[q]
                print(q.guidee.usrinfo.guidee_rating)
        
    usr.guide_lastgdelstseen=timezone.now()
    usr.save()
    return render(request,'gde_contact_lst.html',{'fd':fd,'questions':questions,'new':new,'type':tp})

def gdeprofile(request,field,guidee):
    fd=fields.objects.get(name=field)
    usr_us=User.objects.get(username=str(request.user))
    gde=User.objects.get(username=guidee)
    ques=request.GET.get('ques')
    Q=Question.objects.get(fd=fd,guide=usr_us,guidee=gde,ques=ques)
    Q.status=1
    Q.save()
    print(Q)
    return render(request,'gdeprofile.html',{'ques':ques,'gde':gde})
    



    
    