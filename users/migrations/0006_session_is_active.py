# Generated by Django 3.2.2 on 2021-05-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]