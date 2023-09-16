from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job, RequiredSkill
from .forms import JobPostForm

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
    user = request.user
    jobs = Job.objects.all()
    skills = RequiredSkill.objects.all()
    jobs_count = jobs.count()

    context = {'jobs': jobs, 'jobs_count': jobs_count, 'skills': skills, 'user': user}
    return render(request, 'marketplace/jobs.html', context)
@login_required
def post_job(request):
    # Process the form submitted
    if request.method == 'POST':
        form = JobPostForm(data=request.POSt)
        if form.is_valid():
            job_post = form.save(commit=False)
            # associate the post to user
            job_post.user = request.user
            job_post.save()
            # form sucess message
            return redirect('index')
    else:
        form = JobPostForm()
        
    context = {'form': form}
    return render(request, 'marketplace/post_job.html', context)