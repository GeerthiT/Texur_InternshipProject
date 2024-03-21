from django.shortcuts import render
from Lexicon_App.models import Course

# Create your views here.

def index(request):
    return render(request,"index.html")

def student_login(request):
    return render(request,"student_login.html")


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


