from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Bio, Skill
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    # group = forms.ModelChoiceField(queryset=Group.objects.all())


    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class ProfileEditForm(forms.ModelForm):
    phone_number = PhoneNumberField(region='CA', widget=PhoneNumberPrefixWidget())
    
    class Meta:       
        model = Profile
        fields = ['profile_image', 'phone_number', 'country', 'city']

class BioEditForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields= ['profession', 'bio', 'hourly_rate']

class SkillsEditForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['title']

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_image']