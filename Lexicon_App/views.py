from django.shortcuts import render
from Lexicon_App.models import Course
from .models import User
from django.http import HttpResponseRedirect

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

















































def employer_login(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Save data to the database
        user = User.objects.create(username=username, password=password)
        
        # Redirect to a success page or do any other necessary processing
        return render(request, 'success.html')
    else:
        return render(request, 'employer_login.html')

def employer_singup(request):
    return render(request,"employer_singup.html")
