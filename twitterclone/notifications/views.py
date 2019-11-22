from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required

from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from .models import Notification


@login_required
def notify_user(request):
    html = 'notifications.html'

    all_notifications = Notification.objects.filter(
        notify=request.user.twitteruser)
    # .order_by('-post_date')
    for notification in all_notifications:
        notification.delete()

    return render(request, html, {'all_notifications': all_notifications})