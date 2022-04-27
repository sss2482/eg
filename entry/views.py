from re import template
from urllib import request
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib import auth, messages

from guide.models import guideinfo
from guidee.models import guideeinfo
from .forms import UIform, crtfform
from .models import usrinfo, fields 
from guide.models import Certificate

class sgnup(CreateView):
    form_class=UserCreationForm
    template_name='signup.html'
    success_url=reverse_lazy('fdinfo')
    def form_valid(self, form):
        global rgf
        global usri
        rgf=form
        usri=rgf.save(commit=False)
        return HttpResponseRedirect(self.success_url)
def info(request):
    ch=True
    usr=usri
    if request.method=='POST':
        rp=request.POST
        if 'save' in rp:
            crtf=request.FILES['certificate']
            fd=fields.objects.get(name=rp['fd'])
            ib=rp['issuedby']  
            c=Certificate(usr=usr,fd=fd,issuedby=ib,certificate=crtf)
            c.save()
            usr.guideinfo.certificates.add(c)
            return HttpResponseRedirect(reverse_lazy('login'))
        elif 'save_2' in rp:
            crtf=request.FILES['certificate']
            fd=fields.objects.get(name=rp['fd'])
            ib=rp['issuedby']
            c=Certificate(usr=usr,fd=fd,issuedby=ib,certificate=crtf)
            c.save()
            usr.guideinfo.certificates.add(c)
        else:        
            UIf=UIform(request.POST,request.FILES)
            if UIf.is_valid():
                info=UIf.cleaned_data
                print(info,1,info['DP'])
                rgf.save()
                ui=usrinfo.objects.create(usr=usr,DP=info['DP'])
                gdinf=guideinfo.objects.create(usr=usr)
                gdeinf=guideeinfo.objects.create(usr=usr)
                gdeinf.fds.add(*list(info['fdsneeded']))
                gdinf.fds.add(*list(info['fdsexpert']))
                usr.save()
                print(info['fdsneeded'])
                for fd in list(info['fdsneeded']):
                    uf=fields.objects.get(pk=fd)
                    uf.guidees.add(usri)
                for fd in list(info['fdsexpert']):
                    uf=fields.objects.get(pk=fd)
                    uf.guides.add(usri)
        ch=False
        f=crtfform()
        fds=usr.guideinfo.fds.all()
        return render(request,'info.html',{'form':f,'usr':str(usri),'ch':ch,'fds':fds})
    else:
        f=UIform()
    return render(request,'info.html',{'form':f,'usr':str(usri),'ch':ch})
def logn(request):
    if request.method=='POST':
        usn=request.POST['username']
        pword=request.POST['password']
        ch=auth.authenticate(username=usn,password=pword)
        if ch is not None:
            auth.login(request,ch)
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.info(request,'invalid username or password')
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        return render(request,'registration/login.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))