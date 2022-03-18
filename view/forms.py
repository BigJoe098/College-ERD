from django import forms
from create.models import *

class CustomModelForm(forms.ModelForm):
    
    def is_valid(self):
        result = super().is_valid()

        for item in (self.fields if '__all__' in self.errors else self.errors):
            attrs = self.fields[item].widget.attrs
            attrs.update({'class': attrs.get('class', '') + ' is-invalid'})
        return result

class TeacherForm(CustomModelForm):
    
    class Meta:
        model = teacher 
        fields = '__all__'
        
        exclude = ["teacher_id","create_date"]
          
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'dob': forms.DateInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'department': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
        } 
        
        
class ClassForm(CustomModelForm):
    
    class Meta:
        model = class_model 
        fields = "__all__"
        
        #auto Computed Fields
        exclude = ["class_id","create_date"]
        
        widgets = {
            'semester': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'section': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'department': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
        }
        
        
class DepartmentForm(CustomModelForm):
    
    class Meta:
        model = department 
        fields = "__all__"
        
        #auto Computed Fields
        exclude = ["department_id","create_date"]
        
        widgets = {
            'department_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
        }
        
        
    
class CourseForm(CustomModelForm):
    
    class Meta:
        model = course 
        fields = "__all__"
        
        #auto Computed Fields
        exclude = ["course_id","create_date"]
        
        widgets = {
            'hours': forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'department': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
        }
    

class StudentForm(CustomModelForm):
    
    class Meta:
        model = student 
        fields = "__all__"
        
        #auto Computed Fields
        exclude = ["USN","create_date"]
        
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'dob': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'class_name': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'teacher': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
            'course': forms.Select(attrs={'class': 'form-control form-control-lg', 'disabled' : 'true'}),
        }