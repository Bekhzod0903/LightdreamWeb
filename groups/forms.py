from django import forms
from .models import GroupMessage

class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['text', 'image', 'video', 'audio']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class EditGroupMessageForm(GroupMessageForm):
    class Meta:
        model = GroupMessage
        fields = ['text', 'image', 'video', 'audio']