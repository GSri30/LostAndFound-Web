from django.shortcuts import render,redirect
from lost.models import itemlost
from lost.models import itemfound
from users.models import itemfoundfull,itemlostfull
#from .forms import lostform , foundform,RegistrationForm
from .forms import lostform , foundform
#from.models import RegistrationData 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

from users.forms import lostfullform, foundfullform

from users.models import Profile

from django.core.paginator import Paginator

def lost_view(request,*args,**kwargs):
    obj=itemlost.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }
    return render(request,"lostlist.html",context)
@login_required
def lost_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict1=request.POST.copy()
        dict1['username']=request.user.username
        form=lostform(dict1 or None)
        if form.is_valid():
            formfull=lostfullform(dict1 or None)
            formfull.save()
            form.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form=lostform()
    context={
        'form':form
        }
    return render(request,"lost.html",context)

def found_enter(request,*args,**kwargs):
    if request.method=='POST':
        dict2=request.POST.copy()
        dict2['username']=request.user.username
        form1=foundform(dict2 or None)
        if form1.is_valid():
            formfull1=foundfullform(dict2 or None)
            formfull1.save()
            form1.save()
            messages.success(request,'Your form has been posted successfully!')
            return redirect('home')
    else:
        form1=foundform()
    context={
        'form1':form1
        }
    return render(request,"found.html",context)
@login_required
def found_view(request,*args,**kwargs):
    obj=itemfound.objects.all()
    obj1=list(reversed(obj))
    paginator=Paginator(obj1, 4)
    page=request.GET.get('page') # ?page=number
    objpic=Profile.objects.all()
    context={
        'object':paginator.get_page(page),
        'objectpic':objpic
        }

    return render(request,"foundlist.html",context)



'''def register_view(request,*args,**kwargs):
    context={"formrr":RegistrationForm}
    return render(request,"register.html",context)

def addUser(request,*args,**kwargs):
    formrr = RegistrationForm(request.POST)
    if formrr.is_valid():
        register=RegistrationData(
            username=formrr.cleaned_data['username'],
            password=formrr.cleaned_data['password'],
            rollnumber=formrr.cleaned_data['rollnumber'],
            email=formrr.cleaned_data['email'])
        register.save()
    return redirect('/')'''

