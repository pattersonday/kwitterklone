"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterclone.authentication.urls import urlpatterns as authentication_urls
# from twitterclone.notifications.urls import urlpatterns as notification_urls
from twitterclone.tweets.urls import urlpatterns as tweets_urls
from twitterclone.twitterusers.urls import urlpatterns as twitterusers_urls

from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser

admin.site.register(Tweet)
admin.site.register(TwitterUser)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += authentication_urls
# urlpatterns += notification_urls
urlpatterns += tweets_urls
urlpatterns += twitterusers_urls
