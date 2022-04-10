from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class grp(models.Model):
    name=models.CharField(max_length=200)
    members=models.ManyToManyField(User)

class message(models.Model):
    mssg=models.CharField(max_length=5000)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receiver=models.ForeignKey(User, on_delete=models.CASCADE,related_name="receiver")
    time_send=models.DateTimeField(auto_now_add=True)
    time_received=models.DateTimeField(auto_now=True)

class room(models.Model):
    guide=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usr1")
    guidee=models.ForeignKey(User, on_delete=models.CASCADE, related_name="usr2")
    room_name=models.CharField(max_length=500)
    messages=models.ManyToManyField(message)
    def __str__(self):
        return str(self.room_name)