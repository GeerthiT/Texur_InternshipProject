
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company, Student
from django.contrib.auth.forms import UserCreationForm
# from django.db import models

class admin_reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']






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
   Postal_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
   phone_number= forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
   social_security_number = forms.CharField(widget=forms.NumberInput(attrs={'class' : 'form-control'})) 
 #  COURSE_CHOICES = (
  #      ('', 'Select a course'),  
   #     ('IT Support Technician', 'IT Support Technician'),
    #    ('Frontend Developer', 'Frontend Developer'),
     #   ('ASP.net', 'ASP.net'),
      #  ('Full Stack Developer', 'Full Stack Developer'),
       # ('Python & IT Security', 'Python & IT Security'),
        #('Service now', 'Service now'),
        #('DevOps', 'DevOps'),
        #('Software tester', 'Software tester'),
        
    #)
   #course = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
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
    'Postal_address',
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
    self.fields['Postal_address'].widget.attrs['class'] = 'form-control'
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

class CompanyProfileForm(forms.Form):
    Companyname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Companysize = forms.ChoiceField(choices=[('','Select the Company size'),('Startup','Startup'),('Small','Small'),('Medium','Medium'),('Large','Large'),('Enterprise','Enterprise')], widget=forms.Select(attrs={'class': 'form-control'}))
    Website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    terms_conditions = forms.BooleanField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password fields do not match."
            )

     

def save(self, commit=True):
    if not commit:
        raise NotImplementedError("Can't create Company instance without commit=True")

    # Extract cleaned data
    company_name = self.cleaned_data['Companyname']
    company_size = self.cleaned_data['Companysize']
    website = self.cleaned_data['Website']
    contact_person_name = self.cleaned_data['name']
    contact_person_position = self.cleaned_data['position']
    email = self.cleaned_data['email']
    phone = self.cleaned_data['phone']
    password = self.cleaned_data['password']
    address = self.cleaned_data['address']

    # Saving logic for the company
    company = Company(
        name=company_name,
        size=company_size,
        website=website,
        contact_person_name=contact_person_name,
        contact_person_position=contact_person_position,
        email=email,
        phone=phone,
        address=address
    )
    company.save()

   

    return company