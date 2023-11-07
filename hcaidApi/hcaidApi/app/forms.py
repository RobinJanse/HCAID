from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from hcaidApi.app.models import BadApply, BadPrediction, GoodApply, GoodPrediction

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

class BadApplyForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=True)
    email = forms.EmailField(label='Your email', max_length=100, required=True)
    
    age = forms.CharField(label='Age', max_length=100, required=True)
    gender = forms.BooleanField(label='Is Male', required=False)
    country = forms.CharField(label='Country', max_length=100, required=True)
    seek_help = forms.BooleanField(label='Ever got mental help', required=False)
    tech_company = forms.BooleanField(label='Last worked at company was tech company', required=False)
    remote_work = forms.BooleanField(label='Did you work remotely at your last company', required=False)
    accept_terms = forms.BooleanField(label=mark_safe('I accept the Privacy Policy'), required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class GoodApplyForm(forms.Form):
    name = forms.CharField(label='Your name*', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Your email*', max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    age = forms.IntegerField(label='Age*', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(label="Gender", max_length=100, required=False)
    country = forms.CharField(label='Country*', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    seek_help = forms.BooleanField(label='Ever got mental help', required=False)
    tech_company = forms.BooleanField(label='Last worked at company was tech company', required=False)
    remote_work = forms.BooleanField(label='Did you work remotely at your last company', required=False)
    accept_terms = forms.BooleanField(label=mark_safe('I accept the Privacy Policy*'), required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class GoodPredictionForm(forms.ModelForm):
    class Meta:
        model = BadPrediction
        exclude = []

class BadPredictionForm(forms.ModelForm):
    class Meta:
        model = BadPrediction
        exclude = []