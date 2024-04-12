from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
 
    #def test_adminCompany(self):
    #    response = self.client.get(reverse('company'))
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, 'company.html')

    def test_adminLogin(self):
        response = self.client.get(reverse('admin_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_auth/admin_login.html')

    def test_adminPortal(self):
        response = self.client.get(reverse('welcome_admin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome_admin.html')

    def test_adminCourses(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses.html')

    def test_adminStudents(self):
        response = self.client.get(reverse('students'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students.html')


    #def test_companyLogin(self):
    #    response = self.client.get(reverse('clogin_company'))
    #    self.assertEqual(response.status_code, 200)
    #    self.assertTemplateUsed(response, 'Company_auth/clogin_company.html')

    def test_matchStudent(self):
        response = self.client.get(reverse('profile_matcherStudent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profileMatcher_Student.html')

    def test_matchCompany(self):
        response = self.client.get(reverse('profile_matcherCompany'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profileMatcher_Company.html')

  

   # TEST STUDENT SIGNUP, LOGIN AND INFO PAGES:class StudentViewsTestCase(TestCase):
    class LoginStudentViewTestCase(TestCase):
        def setUp(self):
            self.client = Client()
        
        def test_login_student_view(self):
            # Test GET request to login_student view
            response = self.client.get(reverse('login_student'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'student_auth/login_student.html')
            
            # Create a test user
            user = User.objects.create_user(username='testuser', password='testpassword')
            
            # Test POST request to login_student view with valid credentials
            response = self.client.post(reverse('login_student'), {'username': 'testuser', 'password': 'testpassword'})
            
            # Check if it redirects to info_student page
            self.assertEqual(response.status_code, 302)  # 302 for redirect
            self.assertRedirects(response, reverse('info_student'))

