from django.shortcuts import render
from django.contrib.auth.models import User

from .models import room



def rm(request, other_usr):
    print(other_usr)
    if request.GET.get('requestfrom')=="guide":
        gd=User.objects.get(username=str(request.user))
        gde=User.objects.get(username=str(other_usr))
    elif request.GET.get('requestfrom')=="guidee":
        gde=User.objects.get(username=str(request.user))
        gd=User.objects.get(username=str(other_usr))
    


    try:
        rm=room.objects.get(guide=gd,guidee=gde)
    except:
        room_name=str(gd.username)+"_"+str(gde.username)
        rm=room.objects.create(guide=gd,guidee=gde,room_name=room_name)
        gd.guideinfo.guide_rooms.add(rm)
        gd.save()
        gde.guideeinfo.guidee_rooms.add(rm)
        gde.save()
    
    for mssg in rm.messages.all():
        if mssg.status == "gd1":
            mssg.status="gd2"
            mssg.save()
    
    return render(request, 'chat/room.html', {
        'room': rm,
        'other_usr': other_usr,
        'user_role': request.GET.get('requestfrom'),
    })