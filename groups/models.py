from django.conf import settings
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='group_members')  # Updated related_name

    def __str__(self):
        return self.name

class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='group_images/', blank=True, null=True)
    video = models.FileField(upload_to='group_videos/', blank=True, null=True)
    audio = models.FileField(upload_to='group_audio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.text[:50]}"
