from django.test import TestCase

# Create your tests here.
from higher.gradeapp.forms import AddMarkForm
from higher.gradeapp.models import *


class FormTests(TestCase):

    def test_valid_form(self):
        candidate = Candidate.objects.get(pk=1)
        task = Task.objects.get(pk=1)
        value = '5'
        recruiter = Recruiter.objects.get(pk=1)

        data = {'candidate': candidate, 'task': task, 'value': value, 'recruiter': recruiter}
        form = AddMarkForm(data=data)
        self.assertTrue(form.is_valid())


    def test_invalid_form(self):
        candidate = Candidate.objects.get(pk=1)
        task = Task.objects.get(pk=1)
        value = '5'
        recruiter = Recruiter.objects.get(pk=1)

        data = {'candidate': candidate, 'task': task, 'value': '', 'recruiter': ''}
        form = AddMarkForm(data=data)
        self.assertFalse(form.is_valid())



