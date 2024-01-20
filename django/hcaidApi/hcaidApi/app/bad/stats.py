from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):
    form = request.session.get('form', '')
    prediction = request.session.get('prediction', '')
    shap = request.session.get('shap', '')

    # Feature importances (assuming these are already calculated and normalized)
    feature_importances = {
        'ease_of_medical_leave_for_mental_health': 0.219599,
        'employer_mental_health_resources': 0.118290,
        'employer_seriousness_mental_vs_physical': 0.110994,
        'employer_mental_health_benefits': 0.107426,
        'employer_react_negative_mental_health': 0.100081,
        'awareness_of_mental_health_coverage': 0.100004,
        'employer_discussion_on_mental_health': 0.090216,
        'anonymity_protection': 0.084450,
        'mental_health_impact_on_productivity': 0.036525,
        'observed_consequences_mental_health': 0.032414
    }

    feature_explanations = {
        'ease_of_medical_leave_for_mental_health': 'Very high impact. Easy access to medical leave for mental health strongly correlates with better mental well-being and productivity in the workplace.',
        'employer_mental_health_resources': 'High impact. Availability of mental health resources indicates a supportive work environment, which can significantly improve employee morale and mental health.',
        'employer_seriousness_mental_vs_physical': 'High impact. Employers who value mental health as much as physical health contribute to a more positive and inclusive workplace culture.',
        'employer_mental_health_benefits': 'Medium impact. Offering mental health benefits is a sign of an employer’s commitment to employee well-being, affecting overall job satisfaction.',
        'employer_react_negative_mental_health': 'Medium impact. Negative reactions from employers regarding mental health can create a stressful work environment, impacting employee morale and retention.',
        'awareness_of_mental_health_coverage': 'Medium impact. Awareness of mental health coverage is crucial for employees to feel secure and supported in their workplace.',
        'employer_discussion_on_mental_health': 'Low impact. While discussions on mental health do not directly change workplace policies, they can foster a more open and supportive environment.',
        'anonymity_protection': 'Low impact. Anonymity in seeking mental health resources can encourage more employees to seek help without fear of stigma or repercussions.',
        'mental_health_impact_on_productivity': 'Very low impact. While mental health can affect productivity, other factors often play a more significant role in an employee’s overall performance.',
        'observed_consequences_mental_health': 'Very low impact. Observing negative consequences for coworkers with mental health conditions can affect employee willingness to disclose their own mental health issues.'
    }

    feature_values = {
        'employer_mental_health_benefits': ["I don't know", "Not eligible for coverage / N/A", "No", "Yes"],
        'awareness_of_mental_health_coverage': ["I am not sure", "No", "Yes"],
        'employer_discussion_on_mental_health': ["I don't know", "No", "Yes"],
        'employer_mental_health_resources': ["I don't know", "No", "Yes"],
        'anonymity_protection': ["I don't know", "No", "Yes"],
        'ease_of_medical_leave_for_mental_health': ["I don't know", "Neither easy nor difficult", "Somewhat difficult", "Somewhat easy", "Very difficult", "Very easy"],
        'employer_react_negative_mental_health': ["Maybe", "No", "Yes"],
        'employer_seriousness_mental_vs_physical': ["I don't know", "No", "Yes"],
        'observed_consequences_mental_health': ["No", "Yes"],
        'mental_health_impact_on_productivity': ["No", "Not applicable to me", "Unsure", "Yes"]
    }

    # Prepare the statistics data to pass to the template
    statistics_data = []
    for feature, importance in feature_importances.items():
        explanation = feature_explanations.get(feature, 'No explanation available')

        formatted_importance = "{:.2%}".format(importance)
        statistics_data.append({
            'title': feature.replace('_', ' ').title(),
            'value': feature_values[feature][int(form.get(feature, 0))],
            'importance': formatted_importance,
            'explanation': explanation,
        })

    context = {
        'form': form,
        'prediction': prediction,
        'statistics_data': statistics_data,
    }
    
    return render(request, 'Bad/stats.html', context)