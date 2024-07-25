from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMessage
from .forms import GroupMessageForm

@login_required
def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMessage
from .forms import GroupMessageForm
from .tasks import process_message_task
import threading


@login_required
def group_detail(request, group_id):

    group = get_object_or_404(Group, id=group_id)
    messages = group.messages.all()

    if request.method == 'POST':
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            image = form.cleaned_data.get('image')
            video = form.cleaned_data.get('video')
            audio = form.cleaned_data.get('audio')

            # Start a new thread to process the message
            thread = threading.Thread(target=process_message_task,
                                      args=(group_id, request.user, text, image, video, audio))
            thread.start()

            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupMessageForm()

    return render(request, 'group_detail.html', {'group': group, 'messages': messages, 'form': form})


from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import GroupForm

@user_passes_test(lambda u: u.is_staff)
@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', pk=group.pk)
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMessage
from .forms import EditGroupMessageForm


@login_required
def edit_message(request, group_id, message_id):
    group = get_object_or_404(Group, id=group_id)
    message = get_object_or_404(GroupMessage, id=message_id)

    # Check if the request user is the sender of the message
    if message.sender != request.user:
        return redirect('group_detail', group_id=group.id)

    if request.method == 'POST':
        form = EditGroupMessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = EditGroupMessageForm(instance=message)

    return render(request, 'edit_message.html', {'form': form, 'group': group})


@login_required
def delete_message(request, group_id, message_id):
    group = get_object_or_404(Group, id=group_id)
    message = get_object_or_404(GroupMessage, id=message_id)

    # Check if the request user is the sender of the message
    if message.sender != request.user:
        return redirect('group_detail', group_id=group.id)

    if request.method == 'POST':
        message.delete()
        return redirect('group_detail', group_id=group.id)

    return render(request, 'confirm_delete_message.html', {'message': message, 'group': group})
