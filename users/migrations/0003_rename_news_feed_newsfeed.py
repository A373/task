# Generated by Django 3.2.2 on 2021-05-17 10:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_news_feed_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News_feed',
            new_name='Newsfeed',
        ),
    ]
