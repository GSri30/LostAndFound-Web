from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

from users.models import itemfoundfull
from users.models import itemlostfull


class RegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
#updates username and email        
class UpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

#updates profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']



class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type='time'


class lostfullform(forms.ModelForm):
    product_title = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Title'}))
    #for text field     widget=forms.Textarea()
    place = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'placeholder':'Lost this thing near'}))
    date = forms.DateField(widget=DateInput,label="Date")
    time = forms.TimeField(widget=TimeInput,label="Time")
    description = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Description'}))
    contactme = forms.CharField(max_length=150,label="Contact",widget= forms.TextInput(attrs={'placeholder':'Contact'})) 
    username=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Your username (optional)',}),required=False)
    class Meta:
        model=itemlostfull
        fields=[
            'product_title',
            'place',
            'date',
            'time',
            'description',
            'contactme',
            'username'
        ]

class foundfullform(forms.ModelForm):
    product_title = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Title'}))
    #for text field     widget=forms.Textarea()
    place = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'placeholder':'Found this thing near'}))
    date = forms.DateField(widget=DateInput,label="Date")
    time = forms.TimeField(widget=TimeInput,label="Time")
    description = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Description'}))
    contactme = forms.CharField(max_length=150,label="Contact",widget= forms.TextInput(attrs={'placeholder':'Contact'}))
    username=forms.CharField(max_length=100,widget= forms.TextInput(attrs={'placeholder':'Your username (optional)'}),required=False)
    class Meta:
        model=itemfoundfull
        fields=[
            'product_title',
            'place',
            'date',
            'time',
            'description',
            'contactme',
            'username'
        ]
