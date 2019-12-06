from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import View
from django.utils.decorators import method_decorator

from .models import Tweet
from .forms import AddTweetForm
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification

import re


class Index(View):
    @method_decorator(login_required, name='index')
    def get(self, request):
        html = 'index.html'

        all_tweets = Tweet.objects.all()

        notify_count = Notification.objects.filter(
            notify=request.user.twitteruser).count()

        return render(request, html,
                      {'all_tweets': all_tweets, 'notify_count': notify_count})


def tweet_view(request, id):
    html = 'tweets.html'

    tweet = Tweet.objects.filter(id=id)

    return render(request, html, {'tweet': tweet})


class TweetFormView(View):
    form_class = AddTweetForm
    initial = {'key': 'value'}
    template_name = 'genericform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data
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

        return render(request, self.template_name, {'form': form})
