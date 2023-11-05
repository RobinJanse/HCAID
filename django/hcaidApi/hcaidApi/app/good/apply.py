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
            if form.cleaned_data["accept_terms"] == False:
                print("User did not accept terms")

                return render(request, "good/apply.html", {"form": form, "error": "You must accept the privacy policy."})
            else:
                print("User accepted terms")
                
                databaseInput = GoodApply(
                    age=form.cleaned_data["age"], 
                    gender=form.cleaned_data["gender"], 
                    country=form.cleaned_data["country"], 
                    seek_help=form.cleaned_data["seek_help"], 
                    tech_company=form.cleaned_data["tech_company"], 
                    remote_work=form.cleaned_data["remote_work"]
                )

                #databaseInput.save()
            print(form.cleaned_data)

            print("Age: ", form.cleaned_data["age"])
            print("Gender: ", form.cleaned_data["gender"])

            # Gender can either be Female, Male or Other
            gender = form.cleaned_data["gender"].lower()  # Convert to lowercase
            gender = "Male" if gender == "male" else "Female" if gender == "female" else "Other"

            prediction = model.predict_good(
                form.cleaned_data["age"], 
                form.cleaned_data["gender"], 
                form.cleaned_data["country"], 
                form.cleaned_data["seek_help"], 
                form.cleaned_data["tech_company"], 
                form.cleaned_data["remote_work"]
            )
            #do prediction here
            print("Good model predicted ", prediction)

            request.session["prediction"] = prediction #store prediction in session
            request.session['form'] = form.cleaned_data #store form data in session

            return redirect("/good/stats")
    else:
        form = GoodApplyForm()

    return render(request, "good/apply.html", {"form": form})