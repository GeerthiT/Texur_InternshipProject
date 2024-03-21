from django.shortcuts import render
from Lexicon_App.models import Course, Student, Company

# Create your views here.

def index(request):
    return render(request,"index.html")


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
    data = Course.objects.order_by('course_name')
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


