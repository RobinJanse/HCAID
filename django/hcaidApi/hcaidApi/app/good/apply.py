from django.http import HttpRequest
from hcaidApi.app.forms import GoodApplyForm

from django.shortcuts import render
from django.shortcuts import redirect
from hcaidApi.__init__ import *

from hcaidApi.app.models import GoodApply

def index(request: HttpRequest):

    if request.method == "POST":
        form = GoodApplyForm(request.POST)

        if form.is_valid():
            if form.cleaned_data["privacy_box"] == False:
                print("User did not accept terms")

                return render(request, "good/apply.html", {"form": form, "error": "You must accept the privacy policy."})
            else:
                print("User accepted terms")

                #databaseInput.save()
            print(form.cleaned_data)

            prediction = model.predict_good(
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

            #do prediction here
            print("Good model predicted ", prediction)

            request.session["prediction"] = prediction #store prediction in session
            request.session['form'] = form.cleaned_data #store form data in session

            return redirect("/good/stats")
    else:
        form = GoodApplyForm()

    return render(request, "good/apply.html", {"form": form})