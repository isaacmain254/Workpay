from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Thread, ChatMessage, ThreadMembership
from account.models import Profile

# Create your views here.
@login_required
def messages(request, thread_id=None):
    # retrive all threads associated with the authenticated user
    user = request.user
    threads = Thread.objects.filter(users=user)

    # determine current room on thread_id parameter
    current_room = None
    chat_messages = []
    sender = request.user


    if thread_id:
        current_room = get_object_or_404(Thread, id=thread_id)
        chat_messages = ChatMessage.objects.filter(thread=current_room)
    if thread_id is not None:
    # Get the other user's profile image and name
        other_user = current_room.users.exclude(id=user.id).first()
        if other_user:
            profile = Profile.objects.get(user=other_user)
            other_user_name = other_user.username
            other_user_image = profile.profile_image.url
    else:
        other_user_image  = None
        other_user_name = None
        

     # Create a list of dictionaries containing the thread and other user's username
    thread_info_list = []
    for thread in threads:
        # Assuming you have a field 'sent_by' to track the other user in the thread
        other_user = thread.users.exclude(id=user.id).first()
        if other_user:
            profile = Profile.objects.get(user=other_user)
           
            thread_info_list.append({
                'thread': thread,
                'other_user_username': other_user.username,
                'other_user_profile_image': profile.profile_image.url,
            })

     

    context = {
        'threads': threads,
        'sender':sender,
        'current_room': current_room,
        'chat_messages': chat_messages,
        'thread_info_list': thread_info_list,
        'other_user_name': other_user_name,
        'other_user_image': other_user_image,

    }
    return render(request, 'messages.html', context)


# @login_required
# def messages(request, thread_id):
#     # retrive thread
#     thread = get_object_or_404(Thread, id=thread_id)
#     thread_members = thread.users.all()

#     # chack if the current user is a participant in the thread
#     if request.user not in thread.users.all():
#         return HttpResponseForbidden('You do not have access to this thread')
    
#     # retrive all messages associated with the thread   
#     chat_messages= ChatMessage.objects.filter(thread=thread)
#     sender = request.user
    
#     # sent_to = request.user.exclude()
#     context = {'thread': thread, "chat_messages": chat_messages, 'sender': sender, 'thread_id': thread_id}
#     return render(request, 'messages.html', context)

# view to handle creation or opening of thread
def create_or_open_thread(request, user_id):
    # get the user to start a conversation with
    other_user = User.objects.get(id=user_id)

    # check if a thread already exist between the two users
    thread = Thread.objects.filter(users=request.user).filter(users=other_user).first()
    if thread is None:
        # create thread
        thread = Thread.objects.create()
        ThreadMembership.objects.create(thread=thread, user=request.user)
        ThreadMembership.objects.create(thread=thread, user=other_user)

        # Redirect the user to the chat room
    return redirect('thread-with-messages', thread_id=thread.id)

# chat rooms
def chat_rooms(request):
    user = request.user
    threads = Thread.objects.filter(users=user)
    return render(request)
