from distutils.command.upload import upload
from email.policy import default
from operator import mod
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User



class fields(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    guides=models.ManyToManyField(User,related_name='guides',blank=True)
    guidees=models.ManyToManyField(User,related_name='guidees',blank=True)
    def __str__(self):
        return str(self.name)
def user_directory_path(instance, filename):
    ext=filename.split('.')[-1]
    return '{0}/{1}/{2}'.format(instance.usr.id,'Certificates',filename)
def image_path(instance,filename):
    ext= filename.split('.')[-1]
    filename='{}.{}'.format(str(instance.usr.id)+str('_dp'),ext)
    return '{0}/{1}/{2}'.format(instance.usr.id,'DP',filename)

class Certificates(models.Model):
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    usr=models.ForeignKey(User,on_delete=models.CASCADE)
    issuedby=models.CharField(max_length=500,blank=True)
    certificate=models.FileField(upload_to=user_directory_path,blank=True)
    def __str__(self):
        return str(self.usr)+"_"+str(self.fd)

class Question(models.Model):
    ques=models.TextField()
    fd=models.ForeignKey(fields,on_delete=models.CASCADE)
    guidee=models.ForeignKey(User,related_name="guidee", on_delete=models.CASCADE)
    guide=models.ForeignKey(User, related_name="guide",on_delete=models.CASCADE)
    time_asked=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(default=0)

class usrinfo(models.Model):
    usr=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    fdsneeded=models.ManyToManyField(fields,related_name='interested_fields')
    fdsexpert=models.ManyToManyField(fields,related_name='expertise_fields')
    guide_rating=models.FloatField(default=0.0)
    guidee_rating=models.FloatField(default=0.0)
    level=models.IntegerField(default=0)
    certificates=models.ManyToManyField(Certificates,blank=True)
    DP=models.ImageField(upload_to=image_path,blank=True)
    questions_byguidees=models.ManyToManyField(Question,related_name='questions_byguidees')
    questions_asked=models.ManyToManyField(Question,related_name="questions_asked")
    guide_connectmode=models.IntegerField(default=0)
    guidee_availablemode=models.IntegerField(default=0)
    def __str__(self):
        return str(self.usr)