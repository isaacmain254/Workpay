from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Job, RequiredSkill
from .forms import JobPostForm
from account.models import Profile, Bio, Skill

# Create your views here.
def index(request):
    return render(request, 'marketplace/index.html')

@login_required
def client_page(request):

    freelancers = User.objects.all().order_by('date_joined')
    paginator = Paginator(freelancers, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    freelancers_count = freelancers.count()
    context = {'freelancers': freelancers, 'page_obj': page_obj, 'freelancers_count': freelancers_count}
    return render(request, 'marketplace/freelancers.html', context)

@login_required
def jobs_page(request):
    user = request.user
    #get parameters
    skill_set = request.GET.get('skill') 
    q = request.GET.get('q') 
    check = request.GET.get('check')
    if q or skill_set:
        jobs = Job.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    elif skill_set:
        jobs = Job.objects.filter(Q(title__icontains=skill_set) | Q(description__icontains=skill_set)  )
    elif check:
        jobs = Job.objects.filter(Q(title__icontains=check) | Q(description__icontains=check)  )
    else:
        jobs = Job.objects.all()

    # pagination
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # skills = RequiredSkill.objects.all()
    skills = user.profile.bio.skill_set.all()
    jobs_count = jobs.count()

    context = {'jobs': jobs,'page_obj':page_obj, 'jobs_count': jobs_count, 'skills': skills, 'user': user}
    return render(request, 'marketplace/jobs.html', context)

@login_required
def post_job(request):
    # Process the form submitted
    if request.method == 'POST':
        form = JobPostForm(data=request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            # associate the post to user
            job_post.user = request.user
            job_post.save()
            # saving manytomany model
            form.save_m2m()
            # form sucess message
            return redirect('jobs')
    else:
        form = JobPostForm()
        
    context = {'form': form}
    return render(request, 'marketplace/post_job.html', context)