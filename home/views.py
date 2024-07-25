from .forms import MusicForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Musics
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import NewsForm
from .models import News
# Create your views here.



def landing_page(request):
    return render(request, 'home.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def music_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    musics = Musics.objects.filter(genre=category)
    return render(request, 'music_list.html', {'category': category, 'musics': musics})



@user_passes_test(lambda u: u.is_staff)
def create_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Music successfully added.')
            return redirect('category_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MusicForm()
    return render(request, 'create_music.html', {'form': form})


def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news_list.html', {'news_items': news_items})

@login_required
@user_passes_test(lambda user: user.is_staff)
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from .models import News

def staff_required(function):
    return user_passes_test(lambda u: u.is_staff)(function)

@staff_required
def delete_news(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news_item.delete()
        return redirect('news_list')
    return render(request, 'confirm_delete.html', {'news_item': news_item})
