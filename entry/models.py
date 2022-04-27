from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



class fields(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    guides=models.ManyToManyField(User,related_name='guides',blank=True)
    guidees=models.ManyToManyField(User,related_name='guidees',blank=True)
    def __str__(self):
        return str(self.name)

def image_path(instance,filename):
    ext= filename.split('.')[-1]
    filename='{}.{}'.format(str(instance.usr.id)+str('_dp'),ext)
    return '{0}/{1}/{2}'.format(instance.usr.id,'DP',filename)


class Question(models.Model):
    ques=models.TextField()
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    guidee=models.ForeignKey(User,related_name="guidee", on_delete=models.CASCADE)
    guide=models.ForeignKey(User, related_name="guide",on_delete=models.CASCADE)
    time_asked=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(default=0)
    class Meta:
        ordering=['-time_asked']

class Review(models.Model):
    rvw=models.TextField()
    gd=models.ForeignKey(User, related_name="rvw_guides", on_delete=models.CASCADE)
    gde=models.ForeignKey(User, related_name="rvw_guidees", on_delete=models.CASCADE)
    time_sent=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=15,default="gde_gd")

class Rating(models.Model):
    value=models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)],)
    gd=models.ForeignKey(User, related_name="rating_guides", on_delete=models.CASCADE)
    gde=models.ForeignKey(User, related_name="rating_guidees", on_delete=models.CASCADE)
    status=models.CharField(max_length=15,default='gde_gd')
    time_rated=models.DateTimeField(auto_now=True)


class usrinfo(models.Model):
    usr=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    DP=models.ImageField(upload_to=image_path,blank=True)
    
    def __str__(self):
        return str(self.usr)