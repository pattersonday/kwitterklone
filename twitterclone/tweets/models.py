from django.db import models
from django.utils import timezone
from twitterclone.twitterusers import TwitterUser


class Tweet(models.Model):
    twitter_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    posts = models.CharField(max_length=140)
    post_date = models.DateTimeField(defualt=timezone.now)
