from django.http import HttpRequest
from hcaidApi.app.forms import BadApplyForm

from django.shortcuts import render
from django.shortcuts import redirect
from hcaidApi.__init__ import *

from hcaidApi.app.models import BadApply

def index(request: HttpRequest):

    if request.method == "POST":
        form = BadApplyForm(request.POST)

        if form.is_valid():
            prediction = good_model.predict_dt(
                form.cleaned_data["employer_mental_health_benefits"], 
                form.cleaned_data["awareness_of_mental_health_coverage"], 
                form.cleaned_data["employer_discussed_mental_health"], 
                form.cleaned_data["employer_mental_health_resources"], 
                form.cleaned_data["anonymity_protection"], 
                form.cleaned_data["ease_of_medical_leave_for_mental_health"],
                form.cleaned_data["employer_react_negative_mental_health"], 
                form.cleaned_data["employer_seriousness_mental_vs_physical"], 
                form.cleaned_data["observed_consequences_mental_health"], 
                form.cleaned_data["mental_health_impact_on_productivity"]
            )

            prediction = ["Maybe", "No", "Yes"][prediction]

            request.session["prediction"] = prediction #store prediction in session
            request.session['form'] = form.cleaned_data #store form data in session
            return redirect("/bad/stats")
    else:
        form = BadApplyForm()
        

    return render(request, "bad/apply.html", {"form": form})