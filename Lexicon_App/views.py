from django.shortcuts import render, redirect
from Lexicon_App.models import Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect

# Create your views here.

def index(request):
    return render(request,"index.html")


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





def welcome_admin(request):
    course_count = Course.objects.count()
    context = {
        'course_count': course_count
    }
    return render(request, "welcome_admin.html",context)

def courses(request):
    data = Course.objects.order_by('course_name')
    context = {'course_data': data }
    return render(request,"courses.html", context)

def logout_all_portal(request):
    logout(request)
    return redirect('index')

