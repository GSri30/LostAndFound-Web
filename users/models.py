from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')    

    def __str__(self):
        return f'{self.user.username} Profile'


class itemlostfull(models.Model):
    product_title = models.CharField(max_length=100)
    place = models.TextField(default='Lost this item near ..')
    date = models.DateField()
    time=models.TimeField()
    description = models.TextField()
    contactme = models.CharField(max_length=150,default='email') 
    username=models.CharField(max_length=100,blank=True,default='NULL')

    def __str__(self):
        return f'{self.username} lost {self.product_title}'

class itemfoundfull(models.Model):
    product_title = models.CharField(max_length=100)
    place = models.TextField(default='Found this item near ..')
    date = models.DateField()
    time=models.TimeField()
    description = models.TextField()
    contactme = models.CharField(max_length=150,default='email') 
    username=models.CharField(max_length=100,blank=True,default='NULL')

    def __str__(self):
        return f'{self.username} found {self.product_title}'
