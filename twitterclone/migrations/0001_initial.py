# Generated by Django 2.2.7 on 2019-11-21 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('follower', models.ManyToManyField(related_name='_twitteruser_follower_+', to='twitterclone.TwitterUser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posts', models.CharField(max_length=140)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('twitter_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.TwitterUser')),
            ],
        ),
    ]
