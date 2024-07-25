# tasks.py
import threading
from .models import GroupMessage


def process_message_task(group_id, user, text, image=None, video=None, audio=None):
    """
    Process the message in a separate thread.

    Args:
        group_id (int): The ID of the group where the message is sent.
        user (User): The user who sent the message.
        text (str): The message text.
        image (file, optional): An optional image file.
        video (file, optional): An optional video file.
        audio (file, optional): An optional audio file.
    """
    # Perform the message processing
    GroupMessage.objects.create(
        group_id=group_id,
        sender=user,
        text=text,
        image=image,
        video=video,
        audio=audio
    )
