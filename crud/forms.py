from django.forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class StudentForm(ModelForm):
    class Meta:
     model=Student
     fields='__all__'

class RegirationForm(UserCreationForm):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField()
    mobile=forms.IntegerField()
    


