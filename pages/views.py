from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"index.html",{})

def lost_view(request,*args,**kwargs):
    return render(request,"lost.html",{})

def found_view(request,*args,**kwargs):
    return render(request,"found.html",{})

def about_view(request,*args,**kwargs):
    return render(request,"about us.html",{})

'''def home_after_login_view(request,*args,**kwargs):
    return render(request,"index1.html",{})'''