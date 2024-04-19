from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
 
    def test_adminCompany(self):
        response = self.client.get(reverse('company'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company.html')

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

    def test_studentLogin(self):
        response = self.client.get(reverse('login_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_auth/login_student.html')

    def test_studentSignup(self):
        response = self.client.get(reverse('signup_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_auth/signup_student.html')

    def test_studentInfo(self):
        response = self.client.get(reverse('info_student'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_auth/info_student.html')

    def test_companyLogin(self):
        response = self.client.get(reverse('company_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company_auth/company_login.html')

    def test_matchStudent(self):
        response = self.client.get(reverse('profile_matcherStudent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profileMatcher_Student.html')

    def test_matchCompany(self):
        response = self.client.get(reverse('profile_matcherCompany'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profileMatcher_Company.html')

  

    

