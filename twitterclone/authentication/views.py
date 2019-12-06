from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View

from .forms import LoginForm
from twitterclone.twitterusers.forms import AddTwitterUserForm
from twitterclone.twitterusers.models import TwitterUser


class LoginView(View):
    def get(self, request):
        html = 'login.html'

        if request.method == 'POST':
            login_form = LoginForm(request.POST)

            if login_form.is_valid():
                data = login_form.cleaned_data
                user = authenticate(
                    username=data['username'],
                    password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get(
                        'next', reverse('homepage')
                        )
                )

        login_form = LoginForm()

        return render(request, html, {'login_form': login_form})


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('homepage'))


def register_user_form(request):
    html = 'genericform.html'

    if request.method == 'POST':
        register_form = AddTwitterUserForm(request.POST)

        if register_form.is_valid():
            data = register_form.cleaned_data
            user = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            TwitterUser.objects.create(
                user=user,
                name=data['name']
            )
            return HttpResponseRedirect(reverse('homepage'))

    register_form = AddTwitterUserForm()

    return render(request, html, {'form': register_form})
