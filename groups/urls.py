from django.urls import path
from .views import groups_list, group_detail, create_group, edit_message, delete_message

urlpatterns = [
    path('', groups_list, name='groups_list'),
    path('group/<int:group_id>/', group_detail, name='group_detail'),
    path('group/create/', create_group, name='create_group'),
    path('group/<int:group_id>/message/<int:message_id>/edit/', edit_message, name='edit_message'),
    path('group/<int:group_id>/message/<int:message_id>/delete/', delete_message, name='delete_message'),
]
