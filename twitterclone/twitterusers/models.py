from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    follower = models.ForeignKey(User, related_name='followers+')
    following = models.ForeignKey(User, related_name='followings+')

    def __str__(self):
        return self.name
