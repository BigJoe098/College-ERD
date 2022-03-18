from django.shortcuts import render
from create.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url="")
def Department(request):
    
    OBJ = department.objects.all()
    
    Search = request.POST.get('search')
    if Search == None or Search == "":
        pass
    else:
        OBJ = OBJ.filter(Q(department_id__icontains=Search) | Q(department_name__icontains=Search))
    
    OBJ.order_by("department_id")
    
    paginator = Paginator(OBJ, 5)
    OBJ = paginator.get_page(1)
    
    return render(request, 'department.html', {'departments': OBJ})

@login_required(login_url="")
def Class(request):
    
    OBJ = class_model.objects.all()
     
    Search = request.POST.get('search')
    if Search == None or Search == "":
        pass
    else:
        OBJ = OBJ.filter(Q(class_id__icontains=Search) | Q(name__icontains=Search) | Q(section__icontains=Search) | Q(semester__icontains=Search))
    
    OBJ.order_by("class_id")
    
    paginator = Paginator(OBJ, 5)
    OBJ = paginator.get_page(1)
    
    return render(request, 'class.html', {'classes': OBJ})

@login_required(login_url="")
def Course(request):

    OBJ = course.objects.all()
    
    Search = request.POST.get('search')
    if Search == None or Search == "":
        pass
    else:
        OBJ = OBJ.filter(Q(course_id__icontains=Search) | Q(name__icontains=Search) | Q(hours__icontains=Search))
    
    OBJ.order_by("course_id")
    
    paginator = Paginator(OBJ, 5)
    OBJ = paginator.get_page(1)
    
    return render(request, 'course.html', {'courses': OBJ})

@login_required(login_url="")
def Student(request):

    OBJ = student.objects.all()
    
    Search = request.POST.get('search')
    if Search == None or Search == "":
        pass
    else:
        OBJ = OBJ.filter(Q(USN__icontains=Search) | Q(name__icontains=Search) | Q(sex__icontains=Search))
    
    OBJ.order_by("USN")
    
    paginator = Paginator(OBJ, 5)
    OBJ = paginator.get_page(1)
    
    return render(request, 'student.html', {'students': OBJ})

@login_required(login_url="")
def Teacher(request):
    
    OBJ = teacher.objects.all()
    Search = request.POST.get('search')
    if Search == None or Search == "":
        pass
    else:
        OBJ = OBJ.filter(Q(teacher_id__icontains=Search) | Q(name__icontains=Search) | Q(sex__icontains=Search))
    
    OBJ.order_by("teacher_id")
    
    paginator = Paginator(OBJ, 5)
    OBJ = paginator.get_page(1)
    
    return render(request, 'teacher.html', {'teachers': OBJ})