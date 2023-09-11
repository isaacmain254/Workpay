from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,UserLoginForm, UserEditForm, ProfileEditForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Profile

# Create your views here.
def register(request):
    role = request.GET.get('role')
    print(role)
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
            group = Group.objects.get(name=role)
            new_user.groups.add(group)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

# login 
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('marketplace/client.html')
    else: 
        form = UserLoginForm()
    return render(request, 'account/login.html', {'form': form})

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

def user_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # user = form.save()
            # group = form.cleaned_data['group']
            # group.user_set.add(user)
            return redirect('marketplace/index')
    
    else:
        form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {'form': form})