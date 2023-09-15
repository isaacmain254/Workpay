from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Job, RequiredSkill

# Create your views here.
def index(request):
    return render(request, 'marketplace/index.html')

@login_required
def client_page(request):

    freelancers = User.objects.all()
    freelancers_count = freelancers.count()
    context = {'freelancers': freelancers, 'freelancers_count': freelancers_count}
    return render(request, 'marketplace/freelancers.html', context)

@login_required
def jobs_page(request):
    jobs = Job.objects.all()
    skills = RequiredSkill.objects.all()
    jobs_count = jobs.count()

    context = {'jobs': jobs, 'jobs_count': jobs_count, 'skills': skills}
    return render(request, 'marketplace/jobs.html', context)
