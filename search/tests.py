from django.test import TestCase
from django.shortcuts import render, redirect, reverse
from bugs.models import bug_item
from django.db.models import Q
from django.contrib.auth.models import User
# Create your tests here.

class Test_Bugs_Query(TestCase):
    
    def setUp(self):
        
        name = 'edited bug'
        bug_item.objects.create(name=name)
    
    
    def test_get_bug_search_results(self):
        bug = bug_item.objects.get(name__icontains="edited bug")
        self.assertTrue(bug.name != '')
        self.assertTrue(bug.name == 'edited bug')
        self.assertTrue(bug.description == '')