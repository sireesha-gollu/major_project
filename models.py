from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
class userdata(models.Model):
    user1=models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    phone=models.IntegerField(blank=True)
    address=models.CharField(max_length=100,blank=True)
    profile=models.ImageField(upload_to ='pics')
    '''