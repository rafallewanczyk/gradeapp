from django import forms

from .models import *


class AddMarkForm(forms.Form):
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())
    task = forms.ModelChoiceField(queryset=Task.objects.all())
    value = forms.ChoiceField(choices=[(i,i) for i in range(11)])
    recruiter = forms.ModelChoiceField(queryset=Recruiter.objects.all())


