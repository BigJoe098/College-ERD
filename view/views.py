from django.shortcuts import render
from create.models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url="")
def Teacher(request):
    
    id=request.GET['id']
    instance = teacher.objects.get(teacher_id=id)
    form = TeacherForm(instance=instance)
    std = student.objects.filter(teacher=instance)
    return render(request, "teacher_view.html",{"form":form, 'students' : std})


@login_required(login_url="")
def Student(request):
    
    id=request.GET['id']
    instance = student.objects.get(USN=id)
    form = StudentForm(instance=instance)
    return render(request, "student_view.html",{"form":form})


@login_required(login_url="")
def Department(request):
    
    id=request.GET['id']
    instance = department.objects.get(department_id=id)
    form = DepartmentForm(instance=instance)
    courses = course.objects.filter(department=instance)
    classes = class_model.objects.filter(department=instance)
    teachers = teacher.objects.filter(department=instance)
    return render(request, "department_view.html",{"form":form, 'classes' : classes, 'courses' : courses, 'teachers' : teachers})


@login_required(login_url="")
def Class(request):
    
    id=request.GET['id']
    instance = class_model.objects.get(class_id=id)
    form = ClassForm(instance=instance)
    std = student.objects.filter(class_name=instance)
    return render(request, "class_view.html",{"form":form, 'students' : std})


@login_required(login_url="")
def Course(request):
    
    id=request.GET['id']
    instance = course.objects.get(course_id=id)
    form = CourseForm(instance=instance)
    std = student.objects.filter(course=instance)
    return render(request, "course_view.html",{"form":form, 'students' : std})
