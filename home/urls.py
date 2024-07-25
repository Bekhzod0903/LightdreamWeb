from django.urls import path
from .views import landing_page,category_list,music_list,create_music,news_list,add_news,delete_news

urlpatterns = [
    path('', landing_page, name='home'),
    path('categories/', category_list, name='category_list'),
    path('music/<int:category_id>/', music_list, name='music_list'),
    path('create-music/', create_music, name='create_music'),
    path('news/',news_list, name='news_list'),
    path('news/add/',add_news, name='add_news'),
    path('delete-news/<int:news_id>/', delete_news, name='delete_news'),

]