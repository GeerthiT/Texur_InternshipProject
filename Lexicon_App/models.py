from django.db import models

# Create your models here.

class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    social_security_number = models.CharField(max_length=20)
    postal_address = models.CharField(max_length=200)
    knowledge_level = models.CharField(max_length=100)
    GDPR_consent = models.BooleanField(default=False)
    # class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    # skills = models.ManyToManyField(max_length=100)
    # certifications = models.ManyToManyField(Certification)
    language_proficiency = models.CharField(max_length=200) 
    # internships = models.ManyToManyField(max_length=100)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    github_profile = models.URLField(null=True, blank=True)
    portfolio_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

 

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100) 
    student_ID = models.ManyToManyField(Student) 
    start_date = models.DateField()
    end_date = models.DateField()
   

    def __str__(self):
        return self.name

class Company(models.Model):
    companyID = models.CharField(max_length=100)
    name = models.CharField(max_length=100) 
    contact_details = models.ManyToManyField(Course)
    accepting_interns = models.BooleanField(default=False)
    openings_job_description = models.TextField(blank=True)

    def __str__(self):
        return self.name





