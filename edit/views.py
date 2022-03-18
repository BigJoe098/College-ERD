from django.shortcuts import render,redirect
from django.contrib import messages
from create.models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="")
def Teacher(request):
    
    id=request.GET['id']
    instance = teacher.objects.get(teacher_id=id)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=instance)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Edited.")
        else:
            messages.error(request, "Was Not able to edit new teacher.")
        
        return redirect("/dashboard/teacher")
    
    else:
        form = TeacherForm(instance=instance)
        return render(request, "teacher_edit.html",{"form":form, 'id' : id})
    

@login_required(login_url="")
def Student(request):
    
    id=request.GET['id']
    instance = student.objects.get(USN=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Edited.")
        else:
            messages.error(request, "Was Not able to edit new student.")
        
        return redirect("/dashboard/student")
    
    else:
        form = StudentForm(instance=instance)
        return render(request, "student_edit.html",{"form":form, 'id' : id})
    
    
@login_required(login_url="")
def Department(request):
    
    id=request.GET['id']
    instance = department.objects.get(department_id=id)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=instance)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Edited.")
        else:
            messages.error(request, "Was Not able to edit new department.")
        
        return redirect("/dashboard/department")
    
    else:
        form = DepartmentForm(instance=instance)
        return render(request, "department_edit.html",{"form":form, 'id' : id})
    
    
@login_required(login_url="")
def Class(request):
    
    id=request.GET['id']
    instance = class_model.objects.get(class_id=id)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=instance)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Edited.")
        else:
            messages.error(request, "Was Not able to edit new class.")
        
        return redirect("/dashboard/class")
    
    else:
        form = ClassForm(instance=instance)
        return render(request, "class_edit.html",{"form":form, 'id' : id})
    
    
@login_required(login_url="")
def Course(request):
    
    id=request.GET['id']
    instance = course.objects.get(course_id=id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=instance)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, "Successfully Edited.")
        else:
            messages.error(request, "Was Not able to edit new course.")
        
        return redirect("/dashboard/course")
    
    else:
        form = CourseForm(instance=instance)
        return render(request, "course_edit.html",{"form":form, 'id' : id})