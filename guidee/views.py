from turtle import fd
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render

from entry.models import fields,usrinfo, Question
from django.contrib.auth.models import User
def gdlst(request,field=None):
    if field==None:
        us=User.objects.get(username=str(request.user))
        gds=[]
        for rm in us.usrinfo.guidee_rooms.all():
            gds+=[rm.guide]
        lst_type="contact_lst"
        return render(request,'guidee/gdlst.html',{'gds':gds,'usrinfo':usrinfo,'type':lst_type})
    else:        
        fd=fields.objects.get(name=field)
        gds=fd.guides.all()
        lst_type="fd_gd_lst"
        return render(request,'guidee/gdlst.html',{'gds':gds,'usrinfo':usrinfo,'fd':fd,'type':lst_type})

def gdprofile(request,field,guide):
    gd_us=User.objects.get(username=guide)
    gd=usrinfo.objects.get(usr=gd_us)
    fd=fields.objects.get(name=field)
    usr=User.objects.get(username=str(request.user))
    if request.method=='GET':
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            print(question)
            return render(request,'guidee/gdconnect.html',{'ques':question,'gd':gd,'connect_asked':False})
        else:
            certs=gd.certificates.all()
            certificates=[]
            for c in certs:
                print(c.fd, fd)
                if c.fd == fd:
                    certificates+=[c]
            print(certs, gd, certificates)
            return render(request,'guidee/gdprofile.html',{'gd':gd,'certificates':certificates,'connect_asked':False})
    elif request.method=='POST':
        print("rp")
        if request.GET.get('ques') is not None:
            question=request.GET.get('ques')
            print(question)
            if 'sending_ques' in request.POST:
                print(question)
                Q=Question(ques=question,guide=gd_us,guidee=usr,fd=fd)
                Q.save()
                gd.questions_byguidees.add(Q)
                us=usrinfo.objects.get(usr=usr)
                us.questions_asked.add(Q)
                ques_sent=True
            elif 'unsending_ques' in request.POST:
                Q=Question.objects.get(ques=question,fd=fd,guidee=usr,guide=gd_us)
                us=usrinfo.objects.get(usr=usr)
                us.questions_asked.remove(Q)
                Q.delete()
                ques_sent=False
            return render(request,'guidee/gdconnect.html',{'ques':question,'gd':gd,'ques_sent':ques_sent})


            
            