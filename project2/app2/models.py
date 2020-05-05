from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import tokens


class collage(models.Model):
    collage_name=models.CharField(max_length=80,unique=True)
    reg_number=models.CharField(max_length=20,unique=True)
    addres=models.CharField(max_length=40,unique=True)



class Department(models.Model):
    Department_name=models.CharField(max_length=40,unique=True)
    collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)

class Admin(models.Model):
    name =models.CharField(max_length=20)
    age=models.IntegerField()
    Mob=models.CharField(max_length=20)
    collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE)
    updatedat=models.DateTimeField(auto_now=True)


class Teacher(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()
    Mob=models.CharField(max_length=20)
    collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    createdat=models.DateTimeField(auto_now_add=True)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE)
    updatedat=models.DateTimeField(auto_now=True)


class attdence(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    month=models.CharField(max_length=20)
    count=models.IntegerField()
    working_days=models.IntegerField()
    leave=models.IntegerField()
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)




# Create your models here.
