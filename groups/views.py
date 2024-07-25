from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, GroupMessage
from .forms import GroupMessageForm

@login_required
def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    messages = group.messages.all()
    if request.method == 'POST':
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.group = group
            message.sender = request.user
            message.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupMessageForm()
    return render(request, 'group_detail.html', {'group': group, 'messages': messages, 'form': form})

from django.shortcuts import render, redirect
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


