from django.contrib import admin
from .models import itemlost
#from .models import itemfound,RegistrationData
from .models import itemfound

# Register your models here.
admin.site.register(itemlost)
admin.site.register(itemfound)
#admin.site.register(RegistrationData)