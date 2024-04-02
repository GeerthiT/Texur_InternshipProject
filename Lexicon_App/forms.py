
from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
# from django.db import models


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class RegistrationForm(forms.ModelForm):
   first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
   last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
   username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
   password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
   confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
   email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
   student_ID= forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
   age = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
   
   phone_number= forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
   social_security_number = forms.CharField(widget=forms.NumberInput(attrs={'class' : 'form-control'})) 
   COURSE_CHOICES = (
        ('', 'Select a course'),  
        ('IT Support Technician', 'IT Support Technician'),
        ('Frontend Developer', 'Frontend Developer'),
        ('ASP.net', 'ASP.net'),
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Python & IT Security', 'Python & IT Security'),
        ('Service now', 'Service now'),
        ('DevOps', 'DevOps'),
        ('Software tester', 'Software tester'),
        
    )
   course = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
   linkedin_ID = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
   github_ID = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
   cv = forms.FileField(label='Attach your CV', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
   
    
   class Meta:
        model = Student
        fields = (
    'first_name',
    'last_name',
    'username',
    'password',
    'confirm_password',
    'email',
    'student_ID',
    'social_security_number',
    'phone_number',
    'age',
    'course',
    'linkedin_ID',
    'github_ID',
    'cv',
    
)

def __init__(self, *args, **kwargs):
    super(RegistrationForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs['class'] = 'form-control'
    self.fields['last_name'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password'].widget.attrs['class'] = 'form-control'
    self.fields['confirm_password'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['social_security_number'].widget.attrs['class'] = 'form-control'
    self.fields['age'].widget.attrs['class'] = 'form-control'
    self.fields['student_ID'].widget.attrs['class'] = 'form-control'
    self.fields['phone_number'].widget.attrs['class'] = 'form-control'
    self.fields['linkedin_ID'].widget.attrs['class'] = 'form-control'
    self.fields['github_ID'].widget.attrs['class'] = 'form-control'
    self.fields['cv'].widget.attrs['class'] = 'form-control'





def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)  
    cv_file = self.cleaned_data.get('cv')
    if cv_file:
        user.cv = cv_file
    if commit:
        user.save()
    return user
