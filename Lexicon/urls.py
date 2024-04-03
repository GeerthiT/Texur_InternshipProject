"""
URL configuration for Lexicon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lexicon_App import views
from django.contrib.auth import views as auth_views




urlpatterns = [
   
    path('', views.index, name="index"),
<<<<<<< HEAD
    path('admin_login/', views.admin_login, name="admin_login"),
    path('portal_admin/', views.welcome_admin, name="welcome_admin"),
    path('courses_admin/', views.courses, name="courses"),
    path('logout/', views.logout_all_portal, name='logout'),
   
    path('admin', admin.site.urls),
=======
    path('portal_admin/', views.welcome_admin, name="welcome_admin"),
    path('courses_admin/', views.courses, name="courses"),
    path('login_student/', views.login_student, name="login_student"),
    path('signup_student/', views.signup_student, name="signup_student"),
    path('students/', views.students, name="students"),
    path('company/', views.companies, name="companies"),
    path('search/', views.search, name="search")

>>>>>>> main
]
