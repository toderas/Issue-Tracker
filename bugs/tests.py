from django.test import TestCase
from .models import bug_item
from .forms import AddBugForm
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your tests here.
class bug_itemTests(TestCase):
    """ Defined tests are runing against bug_item model"""
    def test_str(self):
        test_name = bug_item(name='404')
        self.assertEqual(str(test_name), '404')
        
        test_description = bug_item(name='lorem ipsum')
        self.assertNotEqual(str(test_description), 'ipsum lorem')
        self.assertEqual(str(test_description), 'lorem ipsum')
        
        test_date_reported = bug_item(name='2019-08-07 15:31:20.177874')
        self.assertEqual(str(test_date_reported), '2019-08-07 15:31:20.177874')
        self.assertNotEqual(str(test_date_reported), '2019-08-07 15:31:20')
        
        test_author = bug_item(name='john')
        self.assertNotEqual(str(test_author), 'John')
        self.assertEqual(str(test_author), 'john')


    def test_submit_bug_with_missing_fields(self):
        form = AddBugForm(
            {'name': '', 'description': 'lorem ipsum'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
    
    def test_create_bug(self):
        self.user = User.objects.create(username='user')
        self.entry = bug_item.objects.create(name='title', description='body',
                                          author=self.user)
    
    def test_get_all_bugs(self):
        page = self.client.get(reverse('show_bugs'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
