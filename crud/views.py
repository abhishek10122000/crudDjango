from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import *
from crud.forms import RegirationForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login as LoginFun,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def homepage(r):
    return render(r, 'home.html')

def search(r):
    code=r.GET.get('search')
    try:
        searchStudent=StudentForm.objects.filter(Q(fitst_name__icontains=code)|Q(last_name__icontains=code)| Q(mobile__icontains=code))
        return redirect(details,searchStudent.id)
    except:
        return redirect(details)

@login_required()
def details(r):
    studentlist={}
    studentlist['std']=Student.objects.all()
    
    return render(r, 'details.html',studentlist)

@login_required()
def delete(r,id):
    deletes=Student.objects.get(pk=id)
    deletes.delete()
    return redirect(details)

@login_required()
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

@login_required()
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
    form=StudentForm(r.POST or None)
    if r.method=='POST':
        if form.is_valid():
            form.save()
            return redirect(details)
    return render(r, 'apply.html',{'form':form})


