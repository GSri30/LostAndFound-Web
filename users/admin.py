from django.contrib import admin
from .models import Profile
from .models import itemlostfull
#from .models import itemfound,RegistrationData
from .models import itemfoundfull

admin.site.register(Profile)
admin.site.register(itemlostfull)
admin.site.register(itemfoundfull)
