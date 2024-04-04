from django.shortcuts import render, redirect
from Lexicon_App.models import Course, Skillset, Student,Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect



from django.shortcuts import render
from django.contrib import messages
from Lexicon_App.models import Course, Student, Company, Skillset
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from .forms import CompanyProfileForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password


# Create your views here.


def index(request):
    return render(request, "index.html")


# admin_login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('welcome_admin')  
        else:
            # Invalid login, show an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

    # For GET requests or when the login form is initially loaded
    return render(request,"admin_auth/admin_login.html")






@csrf_protect
def login_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In...")
            return redirect('index.html')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, 'student_auth/login_student.html', {})


# def logout_student(request):
#     logout(request)
#     messages.success(request, ("You Have Been Logged Out..."))
#     return redirect('index.html')


def signup_student(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Check if both 'password' and 'confirm_password' exist in cleaned_data
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password and confirm_password:
                if password == confirm_password:
                    # Proceed with user registration
                    user = form.save(commit=False)
                    user.password = make_password(password)  # Manually set hashed password
                    user.save()
                    # Get the selected course ID and skills IDs from the form
                    selected_course_id = request.POST.get('courses')
                    selected_skills_ids = request.POST.getlist('skills')

                    # Save the selected course for the user
                    user.course_id = selected_course_id
                    user.save()

                    # Save the selected skills for the user
                    user.skills.add(*selected_skills_ids)
                    messages.success(request, "Registration successful!")
                    return redirect('login_student')
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Password or Confirm Password is missing.")
        else:
            # Handle form validation errors
            messages.error(request, "Form validation failed.")
    else:
        skills = Skillset.objects.all()
        courses = Course.objects.all()
        for skill in skills:
            print(f"Skill ID: {skill.id}, Name: {skill.name}")
        for course in courses:
            print(f"Course ID: {course.pk}, Name: {course.name}")
        form = RegistrationForm()
    return render(request, 'student_auth/signup_student.html', {'form': form, 'skills': skills, 'courses':courses})



def welcome_admin(request):
    course_count = Course.objects.count()
    context = {
        'course_count': course_count
    }
    return render(request, "welcome_admin.html", context)


def courses(request):
    data = Course.objects.order_by('name')
    context = {'course_data': data }
    return render(request,"courses.html", context)



def logout_all_portal(request):
    logout(request)
    return redirect('index')

def students(request):
    data = Student.objects.order_by('first_name')
    context = {'student_data': data }
    return render(request,"students.html", context)

def companies(request):
    data = Company.objects.order_by('name')
    context = {'company_data': data }
    return render(request,"company.html", context)

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')

        if searched:
            courses = Course.objects.filter(name__icontains=searched)
            students = Student.objects.filter(first_name__icontains=searched)
            companies = Company.objects.filter(name__icontains=searched)

            results = []

            for course in courses:
                results.append({'type': 'course', 'result': course})
            for student in students:
                results.append({'type': 'student', 'result': student})
            for company in companies:
                results.append({'type': 'company', 'result': company})
            
            if not results:
                messages.warning(request, "No search results found.")
            
            return render(request, "search.html", {'searched': searched, 'results': results})
        else:
            messages.warning(request, "Please enter a search term.")
            return render(request, "search.html", {})
    else:
        return render(request, "search.html", {})


def Company_login(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Save data to the database
        user = User.objects.create(username=username, password=password)

        # Redirect to a success page or do any other necessary processing
        return render(request, "success.html")
    else:
        form = RegistrationForm()
    return render(request, "Company_auth/Company_login.html", {"form": form})


def company_signup(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password and confirm_password:
                if password == confirm_password:
                    user = form.save(commit=False)
                    user.password = make_password(password) 
                    user.save()
                    messages.success(request, "Registration successful!")
                    return redirect('Company_login')
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Password or Confirm Password is missing.")
        else:
            messages.error(request, "Form validation failed.")
    else:
        form = CompanyProfileForm()
    return render(request, 'Company_auth/company_signup.html', {'form': form})

