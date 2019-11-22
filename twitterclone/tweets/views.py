from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Tweet
from .forms import AddTweetForm
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification

import re


@login_required
def index(request):
    html = 'index.html'

    all_tweets = Tweet.objects.all()

    notify_count = Notification.objects.filter(notify=request.user.twitteruser).count()

    return render(request, html,
                  {'all_tweets': all_tweets, 'notify_count': notify_count})


def tweet_view(request, id):
    html = 'tweets.html'

    tweet = Tweet.objects.filter(id=id)

    return render(request, html, {'tweet': tweet})


def tweet_form_view(request):
    html = 'genericform.html'

    if request.method == 'POST':
        tweet_form = AddTweetForm(request.POST)

        if tweet_form.is_valid():
            data = tweet_form.cleaned_data
            created_tweet = Tweet.objects.create(
                twitter_user=data['twitter_user'],
                posts=data['posts'],
                post_date=timezone.now()
            )

            if '@' in data['posts']:
                tags = re.findall(r'@(\w+)', data['posts'])
                for tag in tags:
                    target_user = TwitterUser.objects.get(
                        user__username=tag
                    )
                    Notification.objects.create(
                        notify=target_user,
                        tweet_notification=created_tweet
                    )

            return HttpResponseRedirect(reverse('homepage'))

    tweet_form = AddTweetForm()

    return render(request, html, {'form': tweet_form})
