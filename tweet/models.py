from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweets(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.username} - {self.message} - {self.post_date}'
