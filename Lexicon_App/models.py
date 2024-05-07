from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Skillset(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Define a many-to-many relationship with Skillset
    skills = models.ManyToManyField(Skillset)

    def __str__(self):
        return self.name

# Student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    student_ID = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15, default="")
    password = models.CharField(max_length=100, default="")
    confirm_password = models.CharField(max_length=100, default="")
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField("User Email")
    social_security_number = models.CharField(max_length=20)
    postal_address = models.CharField(max_length=200, default='Unknown')
    skills = models.ManyToManyField(Skillset)
    knowledge_level = models.CharField(max_length=100)
    GDPR_consent = models.BooleanField(default=False)
    cv = models.FileField(upload_to="cv/", null=True, blank=True)
    linkedin_ID = models.URLField(null=True, blank=True)
    github_ID = models.URLField(null=True, blank=True)
    course = models.ManyToManyField(Course, related_name="students")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    has_internship = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

 

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    companyID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100, default='')
    accepting_interns = models.BooleanField(default=False)
    openings_internship_description = models.TextField(blank=True)
    required_skills = models.ManyToManyField(Skillset)
    size = models.CharField(max_length=100, default='Unknown')
    website = models.URLField(default='http://example.com')
    contact_person_name = models.CharField(max_length=100, default='Unknown')
    contact_person_position = models.CharField(max_length=100, default='Unknown')
    email = models.EmailField("User Email", default="info@example.com")
    phone = models.CharField(max_length=15, default='Unknown')
    address = models.CharField(max_length=255, default='Unknown')

    def __str__(self):
        return self.name


class InternshipPost(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()


    
class Skill(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Note: Storing passwords in plain text is not secure, consider using Django's built-in authentication system or hashing the passwords

    def __str__(self):
        return self.username

class testStudent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


