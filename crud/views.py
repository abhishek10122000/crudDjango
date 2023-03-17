from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import *
from crud.forms import RegirationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login as LoginFun,logout
# Create your views here.
def homepage(r):
    return render(r, 'home.html')

def details(r):
    studentlist={}
    studentlist['std']=Student.objects.all()
    
    return render(r, 'details.html',studentlist)


def delete(r,id):
    deletes=Student.objects.get(pk=id)
    deletes.delete()
    return redirect(details)

def edit(r,id):
    editStudents=Student.objects.get(pk=id)
    editForm=StudentForm(r.POST or None,instance=editStudents)
    if r.method=='POST':
        if editForm.is_valid():
            editForm.save()
            return redirect(details)
    return render(r, 'edit.html',{'editForm':editForm})

def login(r):
    LoginForm=AuthenticationForm(r.POST or None)
    if r.method=='POST':
            username=r.POST.get('username')
            password=r.POST.get('password')

            user=authenticate(username=username,password=password)
            if user is not None:
                LoginFun(r, user)
                return redirect(homepage)

    return render(r,'login.html',{'form':LoginForm})

def logoutAuth(r):
    logout(r)
    return redirect(login)

def register(r):
    form = StudentForm(r.POST or None)
    if r.method=='POST':
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(r, 'register.html',{'form':form})

def apply(r):
    return render(r, 'apply.html')

# def logout(r):
#     return redirect(homepage)