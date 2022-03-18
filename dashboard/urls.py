from .views import *
from django.urls import path

from . import views

urlpatterns = [
    path('teacher/', views.Teacher, name='teacher'),
    path('student/', views.Student, name='student'),
    path('department/', views.Department, name='department'),
    path('class/', views.Class, name='class'),
    path('course/', views.Course, name='course'),
]