from .models import Profile, Bio, Skill, Project
from django.contrib.auth.models import Group


def create_profile(strategy, backend, user,response, *args, **kwargs):
    """
    Create a user profile for social authentication
    """ 
    print('user is: ', user)
    
    Profile.objects.get_or_create(user=user)
    Bio.objects.get_or_create(profile=user.profile)
    # get or create skills and projects if equal to one 
    # else get all skills and projects belonging to a user
    skills = None
    projects = None
    if skills == 1 or projects == 1:
        skills =  Skill.objects.get_or_create(bio=user.profile.bio)
        projects = Project.objects.get_or_create(bio=user.profile.bio)
    else:
        skills = Skill.objects.filter(bio=user.profile.bio)
        projects = Project.objects.filter(bio=user.profile.bio)

    # Assign user to a group freelancer/client
    role = strategy.session_get('role')
    # User with no choosen group assign group to 'client
    if role is None:
        role = 'client'
    group = Group.objects.get(name=role)
    user.groups.add(group)