from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student, Course, Skillset
from datetime import date

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testadmin', password='testpassword')

        # Create a test student
        self.student = Student.objects.create(
            user=self.user,
            student_ID='123456789',
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
        )

        # Create a test course
        self.course = Course.objects.create(
            name='Test Course',
            start_date=date.today(),
            end_date=date.today()
        )

        # Initialize the test client
        self.client = Client()

    def test_admin_login(self):
        # Test admin login with valid credentials
        response = self.client.post(reverse('admin_login'), {'username': 'testadmin', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect status code

    def test_login_student(self):
        # Test student login with valid credentials
        response = self.client.post(reverse('login_student'), {'username': 'testadmin', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect status code

    def test_display_students(self):
        # Test displaying a list of students
        response = self.client.get(reverse('display_students'))
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_welcome_admin(self):
        # Test displaying welcome page for admin
        response = self.client.get(reverse('welcome_admin'))
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_courses(self):
        # Test displaying courses page
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_student_list(self):
        # Test displaying student list page
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_students(self):
        # Test displaying students page
        response = self.client.get(reverse('students', args=[self.course.pk]))
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_companies(self):
    # Test fetching companies page
        response = self.client.get(reverse('company'))  # Assuming 'company' is the correct URL name
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

    def test_search(self):
        # Test searching for courses, students, and companies
        response = self.client.post(reverse('search'), {'searched': 'test'})
        self.assertEqual(response.status_code, 200)  # Expecting a success status code

   