from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def messages(request):
    sender = request.user
    print('authenticated user', sender)

    return render(request, 'messages.html')