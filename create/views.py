from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect("/accounts/login/")

def login_(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        logout(request)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/dashboard/department")
        else:
            messages.error(request, "Invalid username or password, Please try again.")
            return redirect('/accounts/login/')
    else:
        return render(request, "home.html")

def logout_(request):
    logout(request)
    return redirect('/accounts/login')

@login_required(login_url="")
def Teacher(request):
    
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Created.")    
        else:
            print(form.errors)
            messages.error(request, "Was Not able to create new teacher.")
        
        return redirect("/create/teacher")
    
    else:
        form = TeacherForm()
        return render(request, "teacher_create.html",{"form":form})
    
@login_required(login_url="")
def Class(request):
    
    if request.method == 'POST':
        form = ClassForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Created.")    
        else:
            messages.error(request, "Was Not able to create new class.")
        
        return redirect("/create/class")
    
    else:
        form = ClassForm()
        return render(request, "class_create.html",{"form":form})
    
@login_required(login_url="")
def Department(request):
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Created.")    
        else:
            messages.error(request, "Was Not able to create new Department.")
        
        return redirect("/create/department")
    
    else:
        form = DepartmentForm()
        return render(request, "department_create.html",{"form":form})
    
@login_required(login_url="")
def Course(request):
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Created.")    
        else:
            messages.error(request, "Was Not able to create new Course.")
        
        return redirect("/create/course")
    
    else:
        form = CourseForm()
        return render(request, "course_create.html",{"form":form})
    
@login_required(login_url="")
def Student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Created.")    
        else:
            messages.error(request, "Was Not able to create new Student.")
        
        return redirect("/create/student")
    
    else:
        form = StudentForm()
        print(form)
        return render(request, "student_create.html",{"form":form})