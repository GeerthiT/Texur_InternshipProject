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
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("portal_admin/", views.welcome_admin, name="welcome_admin"),
    path("courses_admin/", views.courses, name="courses"),
    path("company_signup/", views.company_signup, name="company_signup"),
    path("company_login/", views.company_login, name="company_login"),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard'),
    path("login_student/", views.login_student, name="login_student"),
    path("signup_student/", views.signup_student, name="signup_student"),
    path("info_student/", views.info_student, name="info_student"),
    path("students/", views.students, name="students"),
    path("search/", views.search, name="search"),
    path("courses/", views.courses, name="courses"),
    path("company/", views.companies, name="company"),
    path('profileMatcher_Student/', views.profile_matcherStudent, name='profileMatcherStudent'),
    path('profileMatcher_Company/', views.profile_matcherCompany, name='profileMatcherCompany'),
]
