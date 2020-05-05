#from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User

# Create your models here.


class admin1(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    age=models.IntegerField()

def user_save(sender,instance,**kwargs):
    User.objects.create(username=instance.name,password=instance.password)
pre_save.connect(user_save,sender=admin1)


class employee(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    age=models.IntegerField()

def user_save(sender,instance,**kwargs):
    admin1.objects.create(name=instance.name,password=instance.password,age=instance.age)
pre_save.connect(user_save,sender=employee)
