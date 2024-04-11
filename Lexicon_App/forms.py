
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company, Student, Skillset, Course
from django.contrib.auth.forms import UserCreationForm
# from django.db import models

class admin_reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']






class SearchForm(forms.Form):
    query = forms.CharField(label='Search')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'student_ID',
            'social_security_number',
            'phone_number',
            'age',
            'postal_address',
            'linkedin_ID',
            'github_ID',
            'cv',
            'skills',
            'courses',  # Include skills and courses fields here
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

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
