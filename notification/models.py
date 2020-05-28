from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notifications():
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_post = models.DateTimeField(default=timezone.now)
    message_visibility = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.username} - {self.date_post}'