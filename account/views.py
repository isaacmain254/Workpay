from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm,BioEditForm, SkillsEditForm, ProjectUpdateForm
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .models import Profile, Bio, Skill, Project
from django.views.generic import UpdateView



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
            Bio.objects.create(profile=new_user.profile)
            Skill.objects.create(bio=new_user.profile.bio)
            Project.objects.create(bio=new_user.profile.bio)
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
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()  # Save the profile form if it's valid
            return redirect('profile', request.user.id)
        else:
            print('Form is not valid. Failed to save!!')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'account/edit.html', context)

# user profile 
@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    bio = user.profile.bio
    skills = bio.skill_set.all()
    projects = bio.project_set.all()
    context = {'user': user, 'skills': skills, 'projects': projects, 'bio': bio}
    return render(request, 'account/profile.html', context)

# edit user profession details(bio)
@login_required
def edit_bio(request, user_id): 
    bio = get_object_or_404(Bio, id=user_id)
    skills = bio.skill_set.all()

    SkillsFormSet = modelformset_factory(Skill, form=SkillsEditForm, extra=1, can_delete=True)

    if request.method == 'POST':
        bio_form = BioEditForm(instance=bio, data=request.POST)
        skills_formset = SkillsFormSet(request.POST, prefix='skills', queryset=skills)

        if bio_form.is_valid() and skills_formset.is_valid():
            bio_form.save()

            # Save skills with the correct bio reference
            new_skills = skills_formset.save(commit=False)
            for skill in new_skills:
                skill.bio = bio
                skill.save()

            skills_formset.save_m2m()  # Save many-to-many relationships

            return redirect('profile', bio.profile_id)
    else:
        bio_form = BioEditForm(instance=bio)
        skills_formset = SkillsFormSet(prefix='skills', queryset=skills)

    context = {'bio_form': bio_form, 'skills_formset': skills_formset}
    return render(request, 'account/edit-bio.html', context)



# add project
def add_project(request):
    # user = User.objects.get(id=user_id)
    user = request.user
    print(user) 
    
    if request.method == 'POST':
        project_form = ProjectUpdateForm(data=request.POST, files=request.FILES)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            
            new_project.bio = user.profile.bio
            new_project.save()
            return redirect('profile', user.id)
    else:
        project_form = ProjectUpdateForm()
    context = {'project_form': project_form}
    return render(request, 'account/add-project.html', context)
    

# user = request.user
#  Edit an existing project
# project = Project.objects.get(id=project_id)
# project.user = user


# Edit project 
@login_required
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        project_form = ProjectUpdateForm(instance=project, data=request.POST, files=request.FILES)
        if project_form.is_valid():
            project_form.save()
            return redirect('profile', project.bio.id)
    else:
        project_form = ProjectUpdateForm(instance=project)
    context = {'project_form':project_form, 'project': project}
    return render(request, 'account/add-project.html', context)

# delete project
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('profile', project.bio_id)