from django.shortcuts import render, redirect
from Lexicon_App.models import Course, Skillset, Student,Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserForm, StudentForm
from .forms import CompanyProfileForm
from django.contrib.auth.hashers import make_password



def index(request):
    return render(request, "index.html")
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

            error_msg = "Invalid username or password. Try again..."
            context = {'error_msg':  error_msg}if error_msg else {}


            return render(request, 'admin_auth/admin_login.html',context)

            error_msg = "Invalid username or password. Try again..."
            context = {'error_msg':  error_msg}if error_msg else {}


            return render(request, 'admin_auth/admin_login.html',context)

    # For GET requests or when the login form is initially loaded
    return render(request,"admin_auth/admin_login.html")


# student

def login_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        # Check if authentication was successful
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to a success page
            print("successful login")
            return HttpResponseRedirect(reverse('info_student'))
        else:
            # Return an error message or render a login form with error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Render the login form
        return render(request, 'student_auth/login_student.html')

       
def signup_student(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST, request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            student_form.save_m2m()  # Save ManyToManyField data
            return redirect('login_student')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'student_auth/signup_student.html', {'user_form': user_form, 'student_form': student_form})


def info_student(request):
    # Assuming you have a way to identify the current logged-in user
    current_user = request.user

    # Query the Student model to retrieve information for the current user
    try:
        student = Student.objects.get(user=current_user)
    except Student.DoesNotExist:
        # Handle case where student info for the current user does not exist
        student = None

    return render(request, 'student_auth/info_student.html', {'student': student})




def welcome_admin(request):
    course_count = Course.objects.count()
    student_count = Student.objects.count()
    company_count = Company.objects.count()
    navbar_heading = "Welcome to admin portal"
    hi_admin="Hi admin!"

    context = {
        'course_count': course_count,
        'student_count': student_count,
        'company_count': company_count,
        'navbar_heading':navbar_heading,
        'hi_admin':hi_admin
    
    }
    return render(request, "welcome_admin.html",context)


def courses(request):
    data = Course.objects.order_by('name')
    context = {'course_data': data }
    return render(request,"courses.html", context)




def logout_all_portal(request):
    logout(request)
    return redirect('index')

def students(request):
    data = Student.objects.order_by('first_name')
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
                    return redirect('Company_auth/Company_login')
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Password or Confirm Password is missing.")
        else:
            messages.error(request, "Form validation failed.")
    else:
        form = CompanyProfileForm()
    return render(request, "Company_auth/Company_singup.html", {"form": form})
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
                    return redirect('Company_auth/Company_login')
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Password or Confirm Password is missing.")
        else:
            messages.error(request, "Form validation failed.")
    else:
        form = CompanyProfileForm()
    return render(request, "Company_auth/Company_singup.html", {"form": form})
