from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile

# Create your views here.
def index(request):
    return render(request, 'marketplace/index.html')

@login_required
def client_page(request):
    return render(request, 'marketplace/freelancers.html')

@login_required
def jobs_page(request):
    return render(request, 'marketplace/jobs.html')
