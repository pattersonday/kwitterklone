from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Tweets, TwitterUser
from .forms import AddTwitterForm


def user_view(request, id):
    html = 'users.html'

    users = TwitterUser.objects.filter(id=id)

    users_tweets = Tweets.objects.filter(users=id)

    return render(request, html,
                  {'users': users, 'users_tweets': users_tweets})


def user_form_view(request):
    html = 'genericform.html'

    if request.method == 'POST':
        twitter_user_form = AddTwitterForm(request.POST)

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

    twitter_user_form = AddTwitterForm()

    return render(request, html, {'twitter_user_form': twitter_user_form})
