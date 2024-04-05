from django.contrib import admin
from .models import Student, Course, Company, Skillset

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Company)
admin.site.register(Skillset)

