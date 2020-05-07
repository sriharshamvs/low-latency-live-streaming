from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
fs = FileSystemStorage(location='static/photos')
class LiveStreamTheme(models.Model):
    title = models.CharField(max_length=1000)
    stream_key = models.CharField(max_length=50)
    stream_url = models.CharField(max_length=1000)
    comments_server = models.CharField(max_length=1000)
    comments_room = models.CharField(max_length=50)
    img_src = models.ImageField(upload_to=fs)
    description = models.TextField()