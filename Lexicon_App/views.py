from django.shortcuts import render
from django.contrib import messages
from Lexicon_App.models import Course, Student, Company
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")
def admin_login(request):
    return render(request,"admin_login.html")





def student_login(request):
    return render(request,"student_login.html")

def student_signup(request):
    return render(request,"student_signup.html")


def welcome_admin(request):
    course_count = Course.objects.count()
    student_count = Student.objects.count()
    company_count = Company.objects.count()
    context = {
        'course_count': course_count,
        'student_count': student_count,
        'company_count': company_count
    }
    return render(request, "welcome_admin.html", context)

def courses(request):
    data = Course.objects.order_by('name')
    context = {'course_data': data }
    return render(request,"courses.html", context)

def students(request):
    data = Student.objects.order_by('name')
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
            students = Student.objects.filter(name__icontains=searched)
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

