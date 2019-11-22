from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required

from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet


def notification