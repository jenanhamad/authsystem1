from django import forms

from .models import Survey, Answer, Choices

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["title"]