from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company, Student, Skillset, Course
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# from django.db import models


class admin_reg_form(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SearchForm(forms.Form):
    query = forms.CharField(label="Search")


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs["class"] = "form-control"

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class StudentForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skillset.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    courses = forms.ModelChoiceField(
        queryset=Course.objects.all(), empty_label=None, required=True
    )

    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "email",
            "student_ID",
            "profile_picture",
            "social_security_number",
            "phone_number",
            "age",
            "postal_address",
            "linkedin_ID",
            "github_ID",
            "cv",
            "skills",
            "courses",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs["class"] = "form-control"
        self.fields["skills"].widget = (
            forms.CheckboxSelectMultiple()
        )  # Render skills as checkboxes
        self.fields["courses"].widget = forms.RadioSelect()  # Add Bootstrap form-select class to courses dropdown
        

            
class CompanyRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    size = forms.ChoiceField(
        choices=[
            ("", "Select the Company size"),
            ("Startup", "Startup"),
            ("Small", "Small"),
            ("Medium", "Medium"),
            ("Large", "Large"),
            ("Enterprise", "Enterprise"),
        ],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    website = forms.URLField(widget=forms.URLInput(attrs={"class": "form-control"}))
    contact_person_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    contact_details = forms.ChoiceField(
        choices=[
            ("", "Select conatct type"),
            ("Personal", "Personal"),
            ("Office", "Office"),
        ],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone = forms.CharField(
        max_length=15, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    required_skills = forms.ModelMultipleChoiceField(
        queryset=Skillset.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    accepting_interns = forms.BooleanField(required=False)
    terms_conditions = forms.BooleanField(required=True)

    class Meta:
        model = Company
        fields = (
            "name",
            "size",
            "website",
            "contact_person_name",            
            "email",
            "phone",
            "address",
            "required_skills",
            "contact_details"
        )
    def save(self, commit=True):
        company = super().save(commit=False)
        if commit:
            company.save()
            self.save_m2m()
        return company
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class CourseForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skillset.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'custom-skill-field'}))
    new_skill = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Course
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        add_new_skill = kwargs.pop('add_new_skill', True)  # Retrieve the flag indicating whether to include the 'new_skill' field
        super(CourseForm, self).__init__(*args, **kwargs)

        # Retrieve all skills from the database
        all_skills = Skillset.objects.all()
        # Set queryset for the skills field
        self.fields['skills'].queryset = all_skills

        # If the instance has associated skills, mark them as selected
        if 'instance' in kwargs:
            instance = kwargs['instance']
            if instance.pk:
                self.fields['skills'].initial = instance.skills.all()

        if not add_new_skill:
            # Remove the 'new_skill' field from the form
            self.fields.pop('new_skill')

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV file')