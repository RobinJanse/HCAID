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

            if form.cleaned_data["accept_terms"] == False:
                print("User did not accept terms")
                return render(request, "good/apply.html", {"form": form, "error": "You must accept the privacy policy."})
            else:
                print("User accepted terms")
                databaseInput = BadApply(age=form.cleaned_data["age"], gender=form.cleaned_data["gender"], country=form.cleaned_data["country"], seek_help=form.cleaned_data["seek_help"], tech_company=form.cleaned_data["tech_company"], remote_work=form.cleaned_data["remote_work"])
                #databaseInput.save()
            print(form.cleaned_data)


            prediction = model.predict_bad(form.cleaned_data["age"], form.cleaned_data["gender"], form.cleaned_data["country"], form.cleaned_data["seek_help"], form.cleaned_data["tech_company"], form.cleaned_data["remote_work"])
            #do prediction here
            print("Bad model predicted ", prediction)

            request.session["prediction"] = prediction #store prediction in session
            request.session['form'] = form.cleaned_data #store form data in session
            return redirect("/bad/stats")
    else:
        form = BadApplyForm()
        

    return render(request, "bad/apply.html", {"form": form})