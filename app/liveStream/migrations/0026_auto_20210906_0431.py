# Generated by Django 3.0.6 on 2021-09-06 04:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('liveStream', '0025_auto_20210326_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='fdp_details',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ContactDetailFDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email_address', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=100)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('live_stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='liveStream.LiveStream')),
            ],
        ),
    ]
