# Generated by Django 3.0.6 on 2020-05-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveStream', '0004_auto_20200507_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='img_src',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
