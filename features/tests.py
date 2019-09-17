from django.test import TestCase
from .models import Feature
from .forms import AddFeatureForm, ContributeFeatureForm
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.
class Feature_items_Tests(TestCase):
    """ Defined tests are runing against bug_item model"""
    def test_str(self):
        test_name = Feature(name='unicorn')
        self.assertEqual(str(test_name), 'unicorn')

        test_description = Feature(name='description')
        self.assertNotEqual(str(test_description), 'ipsum lorem')
        self.assertEqual(str(test_description), 'description')

        test_date_reported = Feature(name='2019-08-07 15:31:20.177874')
        self.assertEqual(str(test_date_reported), '2019-08-07 15:31:20.177874')
        self.assertNotEqual(str(test_date_reported), '2019-08-07 15:31:20')

        test_author = Feature(name='5')
        self.assertNotEqual(str(test_author), 'John')
        self.assertEqual(str(test_author), '5')

    def test_submit_feature_form_with_missing_fields(self):
        form = AddFeatureForm(
            {'name': '', 'description': 'lorem ipsum'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_get_all_features(self):
        page = self.client.get(reverse('features'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")


class FeatureContributorsTests(TestCase):

    def test_submit_contribute_form_with_wrong_input(self):
        form = ContributeFeatureForm(
           {'amount': 'john'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], [u'Enter a number.'])

    def test_submit_empty_contribute_form(self):
        form = ContributeFeatureForm(
           {'amount': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], [u'This field is required.'])
