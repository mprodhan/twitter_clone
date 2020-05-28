from django.db import models
from django.contrib.auth.models import AbstractUser, User


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length = 30)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.display_name} - {self.joined_date}'
