from django.test import TestCase, Client
from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.views import PasswordResetForm
from django.contrib.auth.models import User
from bugs.views import get_bugs


# Create your tests here.

class TestUserLogin(TestCase):
    def test_login(self):
        form = UserLoginForm({'username': 'user'})
        self.assertFalse(form.is_valid())


    def test_get_login_page(self):
        page = self.client.get(reverse('login'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')


    def test_post_login_with_incorrect_credentials(self):
        self.client = Client()
        self.user = User.objects.create_user('user', 'email@gmail.com', 'password')
        response = self.client.post(reverse('login'), {'username':'Users', 'password':'password'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


    def test_redirect_user_logged_in(self):
        self.client = Client()
        self.user = User.objects.create_user('user', 'email@gmail.com', 'password')
        self.client.login(username='user', password='password')
        response = self.client.get('/bugscurrent-bugs/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
    
    
    def test_get_profile_no_user_logged(self):
        page = self.client.get(reverse('profile'))
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/accounts/login/?next=/accounts/profile/')


class TestUserRegistration(TestCase):
    def test_get_register_page(self):
        page = self.client.get(reverse('registration'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')
    
    
    def test_message_passwords_not_matching(self):
        form = UserRegistrationForm({'password1': 'lepassword', 'password2': 'lepasswword'}) 
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])
    
    
    def test_message_for_missing_fields(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestUserResetPassword(TestCase):
    def test_get_password_reset_page(self):
        page = self.client.get(reverse('password_reset'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration/password_reset_form.html')
    
    
    def test_invalid_email(self):
        form = PasswordResetForm({'email': 'wrongemail'}) 
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'Enter a valid email address.'])
        
        form2 = PasswordResetForm({'email': 'wrongemail@.com'}) 
        self.assertFalse(form2.is_valid())
        self.assertEqual(form2.errors['email'], [u'Enter a valid email address.'])
    
    
    def test_valid_email(self):
        form = PasswordResetForm({'email': 'rightemail@gmail.com'})
        self.assertTrue(form.is_valid())
    
    
