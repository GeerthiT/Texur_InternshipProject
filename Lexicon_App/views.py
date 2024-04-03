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
    return render(request, "index.html")


def welcome_admin(request):
    course_count = Course.objects.count()
    context = {"course_count": course_count}
    return render(request, "welcome_admin.html", context)


def courses(request):
    data = Course.objects.order_by("course_name")
    context = {"course_data": data}
    return render(request, "courses.html", context)


def employer_login(request):
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
    return render(request, "Company_auth/Company_singup.html", {"form": form})
