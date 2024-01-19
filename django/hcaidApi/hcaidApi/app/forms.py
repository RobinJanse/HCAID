from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from hcaidApi.app.models import BadApply, BadPrediction, GoodApply, GoodPrediction

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

class BadApplyForm(forms.Form):
    employer_mental_health_benefits = forms.ChoiceField(
        choices=[
            (3, 'Yes'),
            (0, "I don't know"),
            (2, 'No'),
            (1, "Not eligible for coverage / N/A"),
        ],
        label='Does your employer provide mental health benefits?',
        required=True,
    )

    awareness_of_mental_health_coverage = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I am not sure"),
        ],
        label='Are you aware of the options for mental health care provided by your employer?',
        required=True,
    )

    employer_discussed_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Has your employer ever discussed mental health as part of an employee wellness program?',
        required=True,
    )

    employer_mental_health_resources = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Does your employer provide resources to learn more about mental health issues and how to seek help?',
        required=True,
    )

    anonymity_protection = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?',
        required=True,
    )

    ease_of_medical_leave_for_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Somewhat difficult'),
            (5, 'Very easy'),
            (3, "Somewhat easy"),
            (4, "Very difficult"),
            (0, "I don't know"),
            (1, "Neither easy nor difficult"),
        ],
        label='If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:',
        required=True,
    )

    employer_react_negative_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "Maybe"),
        ],
        label='Do you think that discussing a mental health disorder with your employer would have negative consequences?',
        required=True,
    )

    employer_seriousness_mental_vs_physical = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Do you think that your employer takes mental health as seriously as physical health?',
        required=True,
    )

    observed_consequences_mental_health = forms.ChoiceField(
        choices=[
            (1, 'Yes'),
            (0, 'No'),
        ],
        label='Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?',
        required=True,
    )

    mental_health_impact_on_productivity = forms.ChoiceField(
        choices=[
            (3, 'Yes'),
            (0, 'No'),
            (2, "Unsure"),
            (1, "Not applicable to me"),
        ],
        label='Do you think that discussing a mental health disorder with your employer would have negative consequences?',
        required=True,
    )

    privacy_box = forms.BooleanField(label=mark_safe('I accept the Privacy Policy'), required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class GoodApplyForm(forms.Form):
    employer_mental_health_benefits = forms.ChoiceField(
        choices=[
            (3, 'Yes'),
            (0, "I don't know"),
            (2, 'No'),
            (2, "Not eligible for coverage / N/A"),
        ],
        label='Does your employer provide mental health benefits?',
        required=True,
    )

    awareness_of_mental_health_coverage = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I am not sure"),
        ],
        label='Are you aware of the options for mental health care provided by your employer?',
        required=True,
    )

    employer_discussed_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Has your employer ever discussed mental health as part of an employee wellness program?',
        required=True,
    )

    employer_mental_health_resources = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Does your employer provide resources to learn more about mental health issues and how to seek help?',
        required=True,
    )

    anonymity_protection = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?',
        required=True,
    )

    ease_of_medical_leave_for_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Somewhat difficult'),
            (5, 'Very easy'),
            (3, "Somewhat difficult"),
            (4, "Very difficult"),
            (0, "I don't know"),
            (1, "Neither easy nor difficult"),
        ],
        label='If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:',
        required=True,
    )

    employer_react_negative_mental_health = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "Maybe"),
        ],
        label='Do you think that discussing a mental health disorder with your employer would have negative consequences?',
        required=True,
    )

    employer_seriousness_mental_vs_physical = forms.ChoiceField(
        choices=[
            (2, 'Yes'),
            (1, 'No'),
            (0, "I don't know"),
        ],
        label='Do you think that your employer takes mental health as seriously as physical health?',
        required=True,
    )

    observed_consequences_mental_health = forms.ChoiceField(
        choices=[
            (1, 'Yes'),
            (0, 'No'),
        ],
        label='Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?',
        required=True,
    )

    mental_health_impact_on_productivity = forms.ChoiceField(
        choices=[
            (3, 'Yes'),
            (0, 'No'),
            (2, "Unsure"),
            (1, "Not applicable to me"),
        ],
        label='Do you think that discussing a mental health disorder with your employer would have negative consequences?',
        required=True,
    )

    privacy_box = forms.BooleanField(label=mark_safe('I accept the Privacy Policy'), required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class GoodPredictionForm(forms.ModelForm):
    class Meta:
        model = BadPrediction
        exclude = []

class BadPredictionForm(forms.ModelForm):
    class Meta:
        model = BadPrediction
        exclude = []