# Generated by Django 3.0.6 on 2021-03-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveStream', '0023_livestream_icon_redirect_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='enable_social_media_links',
            field=models.BooleanField(default=False),
        ),
    ]