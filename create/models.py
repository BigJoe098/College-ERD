from django.db import models
from django.db.models.fields import CharField

# Create your models here.

GENDER_CHOICE = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)

class department(models.Model):
    
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200, null=False)
    create_date = models.DateField(auto_now_add=True,null=False)
    
    def __str__(self):
        return self.department_name
    
class class_model(models.Model):
    
    class_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True,null=False)
    semester = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class teacher(models.Model):
    
    teacher_id = models.AutoField(primary_key=True, editable=True)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True,null=False, editable=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=False)
    sex = models.CharField(max_length=50, choices=GENDER_CHOICE, default=1)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class course(models.Model):
    
    course_id = models.AutoField(primary_key=True)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True,null=False)
    name = models.CharField(max_length=200)
    hours = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class student(models.Model):
    
    USN = models.AutoField(primary_key=True)
    class_name = models.ForeignKey(class_model, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(teacher, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(course, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True,null=False)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=False)
    sex = models.CharField(max_length=50, choices=GENDER_CHOICE, default=1)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name