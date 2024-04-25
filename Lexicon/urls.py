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
from Lexicon_App.views import delete_student, update_student
from django.conf.urls.static import static
from django.conf import settings



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

    
    path("update_student/<str:email>/", views.update_student, name="update_student"),
    path("delete_student/<str:email>/", views.delete_student, name="delete_student"),

    path("info_student/<int:student_ID>/", views.info_student, name="info_student"),

    path("students/<int:course_id>", views.students, name="students"),
    
    path("company_signup/", views.company_signup, name="Company_signup"),
    path("search/", views.search, name="search"),
    path("courses/", views.courses, name="courses"),
    #path('courses/<int:course_id>/', views.courses, name='courses'),
    path("student_list/", views.student_list, name="student_list"),
    path("company/", views.companies, name="company"),
    path('profileMatcher_Student/<int:course_id>', views.profile_matcherStudent, name='profile_matcherStudent'),
    path('profile_matcher/<int:course_id>/', views.profile_matcherStudent, name='profile_matcher'),
    path('students/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('students/<int:student_id>/update/', update_student, name='update_student'),
    path('companies/<int:company_id>/delete/', views.delete_company, name='delete_company'),
    path('companies/<int:company_id>/confirm_delete/', views.confirm_company_delete, name='confirm_company_delete'),
    path('update_company/<int:company_id>/', views.update_company, name='update_company'),
    path('send-email/', views.send_email, name='send_email'),
    path("edit_course/<int:course_id>/", views.edit_course, name="edit_course"),
    path("add_student/<int:course_id>/", views.add_student, name="add_student"),
    path("upload_students/<int:course_id>/", views.upload_students, name="upload_students"),
    path("add_course/", views.add_course, name="add_course"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
