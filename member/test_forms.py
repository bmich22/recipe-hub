from django.test import TestCase
from .forms import UserRegistrationForm

# Create your tests here.
class TestUserRegForm(TestCase):
        
    
    def test_form_is_valid(self):
        user_form = UserRegistrationForm({'username': 'name', 'email': 'name@123.com', 'password1': 'test9900', 'password2': 'test9900'})
        self.assertTrue(user_form.is_valid(), msg='Form is not valid')

    
    def test_form_is_invalid(self):
        user_form = UserRegistrationForm({'username': 'name', 'email': 'name@123', 'password1': 'test9900', 'password2': 'test9900'})
        self.assertFalse(user_form.is_valid(), msg='Form is not valid')


    def test_form_is_invalid(self):
        user_form = UserRegistrationForm({'username': 'name', 'email': 'name@123.com', 'password1': 'test9900', 'password2': 'test9999'})
        self.assertFalse(user_form.is_valid(), msg='Form is not valid')