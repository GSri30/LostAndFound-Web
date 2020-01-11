from django.shortcuts import render,redirect
from users.forms import RegistrationForm,UpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from lost.models import itemlost
from lost.models import itemfound
from users.models import itemfoundfull,itemlostfull
#from users.forms import lostfullform , foundfullform
'''
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from lost.models import itemfound,itemlost'''
from django.shortcuts import render, get_object_or_404
from lost.models import itemfound,itemlost

def register(request):
    if request.method=='POST':
        formregi=RegistrationForm(request.POST)
        if formregi.is_valid():
            formregi.save()
            username=formregi.cleaned_data.get('username')
            messages.success(request,f'{username} account has been created successfully! You are now able to login!')
            return redirect('login')
    else:
        formregi=RegistrationForm()
    return render(request,"register.html",{'formregi':formregi})

@login_required
def profile(request):
    return render(request,"profile.html")
@login_required
def updateProfile(request):
    if request.method=='POST':
        u_form=UpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your account has been updated successfully!')
            return redirect('profile')
    else:
        u_form=UpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,"update.html",context)
@login_required
def lost(request):
    obj=itemlostfull.objects.all()
    obj1=reversed(obj)
    context={
        'objectt':obj1,
        }
    return render(request,"lost_specific.html",context)
@login_required
def found(request):
    obj=itemfoundfull.objects.all()
    obj1=reversed(obj)
    context={
        'objectt':obj1,
        }
    return render(request,"found_specific.html",context)
'''
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = itemlost

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.username:
            return True
        return False'''

def post_delete_view(request,id):
    obj=get_object_or_404(itemfound,id=id)
    if request.method=='POST':
        obj.delete()
        messages.success(request,'The post has been deleted from main list successfully!')
        return redirect("found_specific")
    return render(request,"post_delete.html",{"object": obj})

def post_delete_view1(request,id):
    obj1=get_object_or_404(itemlost,id=id)
    if request.method=='POST':
        obj1.delete()
        messages.success(request,'The post has been deleted from main list successfully!')
        return redirect("lost_specific")
    return render(request,"post_delete.html",{"object":obj1})

def specific_post_view(request,id):
    obj=get_object_or_404(itemfound,id=id)
    return render(request,"specific_post_found.html",{"data":obj})

def specific_post_view1(request,id):
    obj1=get_object_or_404(itemlost,id=id)
    return render(request,"specific_post_lost.html",{"data":obj1})

def activelost(request):
    obj=itemlostfull.objects.all()
    obj1=reversed(obj)
    objects=itemlost.objects.all()
    return render(request,"activelost.html",{"objectt":obj1,"objects":objects})

def activefound(request):
    obj=itemfoundfull.objects.all()
    obj1=reversed(obj)
    objects=itemfound.objects.all()
    return render(request,"activefound.html",{"objectt":obj1,"objects":objects})
