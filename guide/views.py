from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.models import User

from entry.models import usrinfo, fields, Question


def gde_cntct_lst(request,field):
    fd=fields.objects.get(name=field)
    us=User.objects.get(username=str(request.user))
    usr=usrinfo.objects.get(usr=us)
    questions=[]
    show=request.GET.get('show')
    if show=='not seen':
        shl=[0,]
    elif show=='all':
        shl=[1,0]
    for q in usr.questions_byguidees.all():
        if q.fd == fd and q.status in shl:
            questions+=[q]
            print(q.guidee.usrinfo.guidee_rating)
            
    return render(request,'gde_contact_lst.html',{'fd':fd,'questions':questions,})

def gdeprofile(request,field,guidee):
    fd=fields.objects.get(name=field)
    us=User.objects.get(username=str(request.user))
    gde=User.objects.get(username=guidee)
    ques=request.GET.get('ques')
    Q=Question.objects.get(fd=fd,guide=us,guidee=gde,ques=ques)
    Q.status=1
    Q.save()
    print(Q)
    return render(request,'gdeprofile.html',{'ques':ques,'gde':gde})
    

    
    