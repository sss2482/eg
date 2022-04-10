from django.shortcuts import render
from django.contrib.auth.models import User
from .models import room


def rm(request, other_usr):
    if request.GET.get('requestfrom')=="guide":
        gd=User.objects.get(username=str(request.user))
        gde=User.objects.get(username=str(other_usr))
    elif request.GET.get('requestfrom')=="guide":
        gde=User.objects.get(username=str(request.user))
        gd=User.objects.get(username=str(other_usr))
    


    try:
        rm=room.objects.get(guide=gd,guidee=gde)
    except:
        room_name=str(gd.username)+"and"+str(gde.username)
        rm=room.objects.create(guide=gd,guidee=gde,room_name=room_name)
    
    return render(request, 'chat/room.html', {
        'room': rm,
        'other_usr': other_usr,
    })