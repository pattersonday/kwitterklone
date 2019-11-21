from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Tweet
from .forms import AddTweetForm


def index(request):
    html = 'index.html'

    all_tweets = Tweet.objects.all()

    return render(request, html, {'all_tweets': all_tweets})


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
            Tweet.objects.create(
                twitter_user=data['twitter_user'],
                posts=data['posts'],
                post_date=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))

    tweet_form = AddTweetForm()

    return render(request, html, {'form': tweet_form})
