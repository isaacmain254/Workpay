from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the choosen password 
            new_user.set_password(user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            # create the user profile 
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# edit user profile details view
@login_required
def edit(request):
    if request.method == 'POST':
        user_form =UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('index')

    else: 
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'account/edit.html', context)