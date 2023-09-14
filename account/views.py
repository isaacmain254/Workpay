from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm,BioEditForm, SkillsEditForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .models import Profile, Bio



# view for user to select group when  navbar  Register button is clicked
# User to select a group before registering
def select_group(request):
    return render(request, 'account/select_group.html')


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
            # Assign user to a group freelancer/client
            group = Group.objects.get(name=role)
            new_user.groups.add(group)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# login redirect view w.r.t user group that is client or freelancer
def login_success(request):
    """
    Redirect users based on whether they are clients or admins
    """
    if request.user.groups.filter(name="client").exists():
        # user is a client 
        return redirect('freelancers')
    else:
        # user is a freelancer
        return redirect('jobs')



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

# user profile 
@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    bios = user.bio_set.all()
    projects = user.project_set.all()
    skills = user.skill_set.all()
    context = {'user': user, 'bios': bios, 'projects': projects, 'skills': skills}
    return render(request, 'account/profile.html', context)

# edit user profession details(bio)
@login_required
def edit_bio(request):
    if request.method == 'POST':
        bio_form = BioEditForm(instance=request.user.bio, data=request.POST)
        skills_form = SkillsEditForm(instance=request.user.skill, data=request.POST)

        if bio_form.is_valid() and skills_form.is_valid():
            bio_form.save()
            skills_form.save()
            return redirect('index')
        
    else:
        bio_form = BioEditForm(instance=request.user.bio)
        skills_form = SkillsEditForm(instance=request.user.skill)
    return render(request, 'account/edit-bio.html', {'bio_form': bio_form, 'skills_form': skills_form})



