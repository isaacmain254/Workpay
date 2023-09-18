from django import forms
from .models import Job,RequiredSkill

class JobPostForm(forms.ModelForm):
    # required_skills = forms.ModelMultipleChoiceField(queryset=RequiredSkill.objects.all(), widget=forms.TextInput )
    class Meta:
        model = Job
        fields = ['title', 'description', 'required_skills', 'budget']

class SkillForm(forms.ModelForm):
    class Meta:
        model = RequiredSkill
        fields = ['required_skill']

class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)