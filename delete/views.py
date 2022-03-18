from django.shortcuts import redirect
from create.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="")
def Teacher(request):
    
    id=request.GET['id']
    instance = teacher.objects.get(teacher_id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("/dashboard/teacher/")

@login_required(login_url="")
def Student(request):
    
    id=request.GET['id']
    instance = student.objects.get(USN=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("/dashboard/student/")

@login_required(login_url="")
def Department(request):
    
    id=request.GET['id']
    instance = department.objects.get(department_id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("/dashboard/department/")

@login_required(login_url="")
def Class(request):
    
    id=request.GET['id']
    instance = class_model.objects.get(class_id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("/dashboard/class/")

@login_required(login_url="")
def Course(request):
    
    id=request.GET['id']
    instance = course.objects.get(course_id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("/dashboard/course/")
