from django.test import TestCase
from .models import bug_item

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
        
        

