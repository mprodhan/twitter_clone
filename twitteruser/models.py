from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length = 30)
    joined_date = models.DateTimeField(auto_now_add=True)
    # twitter_following = models.ManyToManyField(symmetrical=False)

    def __str__(self):
        return f'{self.display_name} - {self.joined_date}'
