# Generated by Django 3.2.2 on 2021-05-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_session_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
