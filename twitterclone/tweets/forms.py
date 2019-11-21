from django import forms
from .models import Tweet


class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'twitter_user',
            'posts',
            'post_date'
        ]
