from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail


from .models import Job, RequiredSkill
from .forms import JobPostForm, ContactForm
from account.models import Profile, Bio, Skill



#landing page also handles form submission and sending email
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            # recipient_list = ['elliotlinkon@gmail.com'] 
            send_mail(subject, message, sender_email, ['elliotlinkon@gmail.com'])
            messages.success(request, "Email sent successfully" )
            return redirect('email-success')
    else:
        form = ContactForm()
    return render(request, 'marketplace/index.html', {'form': form})


# Email success
def email_success(request):
    return render(request, 'marketplace/email_success.html')


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
    if q :
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