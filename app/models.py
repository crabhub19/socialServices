from django.db import models
from .baseModel import BaseModel
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class District(BaseModel):
    name = models.CharField(max_length=25,null=True,blank=True)
    def __str__(self):
        return self.name

class Worker(BaseModel):
    name = models.CharField(max_length=25,null=True,blank=True)
    workerImage = models.ImageField(upload_to="workerImage",blank=True,null=True)
    def __str__(self):
        return self.name

class Users(BaseModel):
    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    contracNo   = models.CharField(max_length=25,null=True,blank=True)
    gender      = models.CharField(max_length=12,null=True,blank=True)
    userImage   = models.ImageField(upload_to="userImage",blank=True,null=True)
    localAddress= models.CharField(max_length=12,null=True,blank=True)
    worker      = models.ForeignKey(Worker,on_delete=models.CASCADE,blank=True,null=True)
    district    = models.ForeignKey(District,on_delete=models.CASCADE,blank=True,null=True)
    active      = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username



