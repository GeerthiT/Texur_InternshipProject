from django.shortcuts import render, redirect, get_object_or_404
from Lexicon_App.models import Course, Skillset, Student,Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
import csv
from io import TextIOWrapper
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import UserForm, StudentForm, CompanyProfileForm, CourseForm, CSVUploadForm, UserRegistrationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db import IntegrityError


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
            student = Student.objects.get(user=user)
            return HttpResponseRedirect(reverse('info_student', args=[student.student_ID]))
        else:
            # Return an error message or render a login form with error message
            return render(request, 'student_auth/login_student.html', {'error_message': 'Invalid username or password'})
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


def info_student(request, student_ID):
    # Query the Student model to retrieve information for the specified student ID
    student = get_object_or_404(Student, student_ID=student_ID)
    
    return render(request, 'student_auth/info_student.html', {'student': student})


#Update a Student
def update_student(request, email):
    # Retrieve the student object using the provided email
    student = get_object_or_404(Student, email=email)

    if request.method == 'POST':
        # Populate the update form with current student data and submitted data
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            # Save the updated student object to the database
            form.save()
            return redirect('info_student', student_ID=student.student_ID)  # Redirect to student info page or any relevant page
    else:
        # If the request method is GET, display the update form populated with current student data
        form = StudentForm(instance=student)

    return render(request, 'student_auth/update_student.html', {'form': form, 'student': student})

# Delete a Student
def delete_student(request, email):
    # Retrieve the student object using the provided ID
    student = get_object_or_404(Student, email=email)
    # Delete the student from DB
    student.delete()
    # Redirect to a relevant page
    return redirect ('students')



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
    #print(context)
    return render(request,"courses.html", context)

def student_list(request):
    data = Course.objects.order_by('name')
    context = {'course_data': data }
    #print(context)
    return render(request,"student_auth/student_list.html", context)


def logout_all_portal(request):
    logout(request)
    return redirect('index')

def students(request, course_id):
    # Get the course object based on the course ID
    course = get_object_or_404(Course, pk=course_id)
    
    # Filter students enrolled in the specific course
    student_data = course.students.all().order_by('first_name')
    
    context = {'student_data': student_data, 'course': course }
    return render(request, "students.html", context)

def companies(request):
    data = Company.objects.order_by('name')
    context = {'company_data': data }
    return render(request,"company.html", context)

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')

        if searched:
            # Search for courses, students, and companies matching the searched term
            courses = Course.objects.filter(name__icontains=searched)
            students = Student.objects.filter(Q(first_name__icontains=searched) | Q(last_name__icontains=searched) | Q(skills__name__icontains=searched))
            companies = Company.objects.filter(Q(name__icontains=searched) | Q(required_skills__name__icontains=searched))

            results = []

            # Append search results to the results list
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

    # company  views.py starts
    
def company_login(request):
    if request.method == "POST":
        # Get data from the form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            print("successful login")
            return redirect('index')  
        else:
            # Authentication failed, handle it appropriately (e.g., show error message)
            error_message = "Invalid username or password."
            return render(request, "company_auth/company_login.html", {"form": UserRegistrationForm(), "error_message": error_message})
    else:
        form = UserRegistrationForm()
        return render(request, "company_auth/company_login.html", {"form": form})
        


def company_signup(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            company_name = form.cleaned_data['company_name']
            company_size = form.cleaned_data['company_size']
            website = form.cleaned_data['website']
            contact_person_name = form.cleaned_data['contact_person_name']
            contact_person_position = form.cleaned_data['contact_person_position']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']

            # Create User instance
            user = User.objects.create_user(username=email, email=email, password=password)

            # Create Company instance and associate with user
            company = Company.objects.create(
                user=user,  # Assign the user to the company
                name=company_name,
                size=company_size,
                website=website,
                contact_person_name=contact_person_name,
                contact_person_position=contact_person_position,
                email=email,
                phone=phone,
                address=address
            )

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                print("successful login")
                return redirect('company_login')
            else:
                # Authentication failed, handle it appropriately (e.g., show error message)
                error_message = "Failed to authenticate user."
                return render(request, "company_auth/company_signup.html", {"form": form, "error_message": error_message})
        else:
            messages.error(request, "Form validation failed.")
    else:
        form = CompanyProfileForm()
    return render(request, "company_auth/company_signup.html", {"form": form})



def company_dashboard(request):
    company_info = request.user.company_profile  
    InternshipPost = InternshipPost.objects.filter(company=company_info)
    return render(request, 'company_auth/company_dashboard.html', {'company_info': company_info, 'Internship_Post': InternshipPost})


# Delete a company
def delete_company(request, company_id):
    # Retrieve the company object using the provided ID
    company = get_object_or_404(Company, pk=company_id)
    # Delete the company from the database
    company.delete()
    # Redirect to a relevant page
    return redirect('company')  

def confirm_company_delete(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'confirm_company_delete.html', {'company': company})

# Update a company
def update_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_profile')  # Redirect to the company profile page after successful update
    else:
        form = CompanyUpdateForm(instance=company)
    return render(request, 'update_company.html', {'form': form}) 

  # internship views.py 




def profile_matcherStudent(request, course_id):
    # Retrieve the course object
    course = Course.objects.get(pk=course_id)

    # Retrieve all students associated with the course
    students = course.students.all()

    # Initialize an empty dictionary to store matched student-company pairs
    matched_pairs = {}

    # Iterate through each student
    for student in students:
        # Retrieve the skills of the student
        student_skills = student.skills.all()

        # Find companies that match the student's skills and the course's associated skills
        matching_companies = []
        for company in Company.objects.all():
            # Retrieve the required skills of the company
            required_skills = company.required_skills.filter(course=course)
            # Find common skills between student and company
            common_skills = set(student_skills).intersection(required_skills)
            if common_skills:
                matching_companies.append({
                    'company': company,
                    'common_skills': common_skills
                })

        # Store the matched companies for the current student
        if matching_companies:
            matched_pairs[student] = matching_companies

    # Pass the matched_pairs dictionary to the template for rendering
    return render(request, 'profileMatcher_Student.html', {'matched_pairs': matched_pairs})



def profile_matcherCompany(request):
    # Retrieve all students
    companies = Company.objects.all()

    # Initialize an empty dictionary to store matched student-company pairs
    matched_pairs = {}

    # Iterate through each company
    for company in companies:
        # Retrieve the skills of the student
        required_skills = company.required_skills.all()

        # Find companies that match the student's skills
        matching_students = []
        for student in Student.objects.all():
            # Retrieve the required skills of the company
            student_skills = student.skills.all()
            # Find common skills between student and company
            common_skills = set(student_skills).intersection(required_skills)
            if common_skills:
                matching_students.append({
                    'student': student,
                    'common_skills': common_skills
                })

        # Store the matched companies for the current student
        if matching_students:
            matched_pairs[company] = matching_students
   # Pass the matched_pairs dictionary to the template for rendering
    return render(request, 'profileMatcher_Company.html', {'matched_pairs': matched_pairs})
    

#@login_required
def send_email(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
        except ObjectDoesNotExist:
            return HttpResponse('Student not found!', status=404)
        
        # Replace the below with your actual email sending logic
        send_mail(
            'Subject',
            'Message body',
            'sender@example.com',
            [student.email],
            fail_silently=False,
        )
        return redirect('email_sent')  # Redirect to a confirmation page
    else:
        return HttpResponse('Invalid request!', status=400)

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # Save the course object without committing to the database yet
            course = form.save(commit=False)
            course.save()

            # Process skills
            skills = request.POST.getlist('skills')  # Existing skills
            new_skill_name = request.POST.get('new_skill')  # New skill entered by the user

            for skill_id in skills:
                if skill_id.startswith('new_'):
                    # If it's a new skill, create it and associate it with the course
                    new_skill_name = skill_id.replace('new_', '').replace('-', ' ')
                    skill, created = Skillset.objects.get_or_create(name=new_skill_name)
                    course.skills.add(skill)
                else:
                    # If it's an existing skill, add it to the course
                    skill = Skillset.objects.get(pk=skill_id)
                    course.skills.add(skill)
            print(course)
            # Save the course object with the associated skills
            course.save()

            # Redirect to avoid form resubmission
            return redirect('courses')
    else:
        form = CourseForm()

    # Retrieve all skills from the database
    all_skills = Skillset.objects.all()
    # Pass both all_skills and course_skills to the form
    course_skills = request.POST.getlist('skills')
    form = CourseForm(initial={'skills': course_skills})
    print(course_skills)
    return render(request, 'course_administration/add_course.html', {'form': form, 'all_skills': all_skills})

def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            # Save the form data without committing to the database yet
            course = form.save(commit=False)
            
            # Get the selected skills from the form data
            selected_skill_ids = request.POST.getlist('skills')
            selected_skills = Skillset.objects.filter(pk__in=selected_skill_ids)
            
            # Clear existing skills and add selected skills
            course.skills.clear()
            course.skills.add(*selected_skills)
            
            # Save the course object to update the changes in the database
            course.save()
            
            # Check if a flag indicating the need to update students is set
            if request.POST.get('update_students'):
                return redirect('upload_students', course_id=course_id)
            else:
                return redirect('courses')
    else:
        # Retrieve all skills from the database
        all_skills = Skillset.objects.all()
        # Retrieve the skills associated with the course
        course_skills = course.skills.all()
        
        # Pass both all_skills and course_skills to the form
        form = CourseForm(instance=course, initial={'skills': course_skills})
    
    return render(request, 'course_administration/edit_course.html', {'form': form, 'course_id': course_id, 'all_skills': all_skills, 'course_skills': course_skills})


def add_student(request, course_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Extract password from form data
            password = form.cleaned_data['password']

            # Create a new User object
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=password  # Use provided password
            )

            # Create a new Student object and associate it with the user
            student = form.save(commit=False)
            student.user = user
            student.save()
            
            # Retrieve the course and add the student to it
            course = Course.objects.get(pk=course_id)
            course.students.add(student)
            
            return redirect('edit_course', course_id=course_id)
    else:
        form = StudentForm()
    return render(request, 'course_administration/add_student.html', {'form': form, 'course_id': course_id})

def upload_students(request, course_id):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file:
            messages.error(request, 'No file selected')
            return redirect('edit_course', course_id=course_id)

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Invalid file format. Please upload a CSV file.')
            return redirect('edit_course', course_id=course_id)

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.reader(decoded_file, delimiter=';')
        course = Course.objects.get(pk=course_id)  # Retrieve the course instance

        for row in csv_reader:
            if len(row) < 3:
                messages.warning(request, f'Skipping row: {row}. Each row should contain at least First Name, Last Name, and Email.')
                continue

            first_name, last_name, email = row[:3]  # Extract first name, last name, and email from the row
            
            # Assuming you have a mechanism to create or retrieve users based on email
            user, created = User.objects.get_or_create(email=email, defaults={'username': email})
            
            # Check if a Student object already exists for this user
            student, student_created = Student.objects.get_or_create(user=user)
            
            # Update the student details if it was already created
            if not student_created:
                student.first_name = first_name
                student.last_name = last_name
                student.save()
            else:
                student.first_name = first_name
                student.last_name = last_name
                student.save()
            
            course.students.add(student)

        messages.success(request, 'Students uploaded successfully.')
        return redirect('edit_course', course_id=course_id)
    else:
        messages.error(request, 'Invalid request method')
        return redirect('edit_course', course_id=course_id)

