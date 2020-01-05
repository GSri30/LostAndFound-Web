from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile
'''
from users.models import itemfoundfull
from users.models import itemlostfull
from lost.models import itemfound
from lost.models import itemlost'''

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

'''
@receiver(post_save,sender=itemfound)
def create_itemfound(sender,instance,created,**kwargs):
    if created:
        itemfoundfull.objects.create()'''

