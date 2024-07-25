from django.urls import path
from . import views

urlpatterns = [
    path('', views.groups_list, name='groups_list'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('create-group/', views.create_group, name='create_group'),

]
