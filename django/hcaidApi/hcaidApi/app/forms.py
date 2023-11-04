from django import forms
from django.utils.html import format_html

from hcaidApi.app.models import BadApply, BadPrediction

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

    accept_terms = forms.BooleanField(label= format_html('I accept the <a href="/good/privacy">Privacy Policy</a>'), required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class BadPredictionForm(forms.ModelForm):
    class Meta:
        model = BadPrediction
        exclude = []


