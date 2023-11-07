from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):

    form = request.session.get('form', '')
    prediction = request.session.get('prediction', '')

    print("Pred2 from stats", prediction)
    print("form2 from stats", form)

    prediction_accepted = "Yes" if prediction == 1 else "No"

    # Prepare the statistics data to pass to the template
    statistics_data = [
        {'title': 'Prediction Value', 'value': prediction_accepted},
        {'title': 'Name', 'value': form.get('name', '')},
        {'title': 'Email', 'value': form.get('email', '')},
        {'title': 'Age', 'value': form.get('age', '')},
        {'title': 'Gender', 'value': form.get('gender', '')},
        {'title': 'Country', 'value': form.get('country', '')},
        {'title': 'Seek Help', 'value': form.get('seek_help', '')},
        {'title': 'Tech Company', 'value': form.get('tech_company', '')},
        {'title': 'Remote Work', 'value': form.get('remote_work', '')}
    ]

    context = {
        'form': form,
        'prediction': prediction,
        'statistics_data': statistics_data,
    }

    return render(request, 'good/stats.html', context)
