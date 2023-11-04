from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):

    form = request.session.get('form', '')
    prediction = request.session.get('prediction', '')

    print("Pred2 from stats" , prediction)
    print("form2 from stats" , form)

    return render(request, 'bad/stats.html')