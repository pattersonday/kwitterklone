from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    html = 