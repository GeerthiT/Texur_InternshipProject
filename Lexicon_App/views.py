from django.shortcuts import render
from django.contrib import messages
from Lexicon_App.models import Course, Student, Company
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    return render(request,"index.html")


def welcome_admin(request):
    course_count = Course.objects.count()
    context = {
        'course_count': course_count
    }
    return render(request, "welcome_admin.html", context)

def courses(request):
    data = Course.objects.order_by('course_name')
    context = {'course_data': data }
    return render(request,"courses.html", context)


def Company_login(request):
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
         return render(request, 'Company_auth/Company_login.html', {})


def Company_singup(request):
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
        form = RegistrationForm()
    return render(request,"Company_auth/Company_singup.html",{'form': form})
