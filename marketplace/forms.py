from django import forms
from .models import Job,RequiredSkill

class JobPostForm(forms.ModelForm):
    # required_skills = forms.ModelMultipleChoiceField(queryset=RequiredSkill.objects.all(), widget=forms.TextInput )
    class Meta:
        model = Job
        fields = ['title', 'description', 'required_skills', 'budget']