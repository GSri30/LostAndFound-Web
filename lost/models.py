from django.db import models

# Create your models here.
class itemlost(models.Model):
    product_title = models.CharField(max_length=100)
    place = models.TextField(default='Lost this item near ..')
    date = models.DateField()
    time=models.TimeField()
    description = models.TextField()
    contactme = models.CharField(max_length=150,default='email') 
    username=models.CharField(max_length=100,blank=True,default='NULL')

    def __str__(self):
        return f'{self.username} lost {self.product_title}'

class itemfound(models.Model):
    product_title = models.CharField(max_length=100)
    place = models.TextField(default='Found this item near ..')
    date = models.DateField()
    time=models.TimeField()
    description = models.TextField()
    contactme = models.CharField(max_length=150,default='email') 
    username=models.CharField(max_length=100,blank=True,default='NULL')

    def __str__(self):
        return f'{self.username} found {self.product_title}'


'''class RegistrationData(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    rollnumber=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.username'''
