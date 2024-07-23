from .models import News
from django import forms
from .models import Musics

class MusicForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = ['title', 'artist', 'genre', 'music']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'video']
