from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from twitterclone.tweets.models import Tweet
from .models import TwitterUser
from .forms import AddTwitterUserForm


def user_view(request, id):
    html = 'users.html'

    users = TwitterUser.objects.filter(id=id)

    users_tweets = Tweet.objects.filter(twitter_user=id)

    following_count = users.first().following.count()

    return render(request, html,
                  {'users': users, 'users_tweets': users_tweets, 'following_count': following_count})


def user_form_view(request):
    html = 'genericform.html'

    if request.method == 'POST':
        twitter_user_form = AddTwitterUserForm(request.POST)

        if twitter_user_form.is_valid():
            data = twitter_user_form.cleaned_data
            user = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            TwitterUser.objects.create(
                user=user,
                name=data['name']
            )
            return HttpResponseRedirect(reverse('homepage'))

    twitter_user_form = AddTwitterUserForm()

    return render(request, html, {'form': twitter_user_form})


def following_view(request, id):

    following = TwitterUser.objects.get(id=id)

    request.user.twitteruser.following.add(following)

    return HttpResponseRedirect(reverse('user', args=(id,)))


def unfollow_view(request, id):

    unfollow = TwitterUser.objects.get(id=id)

    request.user.twitteruser.following.remove(unfollow)

    return HttpResponseRedirect(reverse('user', args=(id,)))
