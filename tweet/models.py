from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    message = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.twitteruser} - {self.message} - {self.post_date}'
