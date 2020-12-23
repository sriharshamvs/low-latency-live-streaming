from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
fs = "gallery"
class LiveStream(models.Model):
    title = models.CharField(max_length=1000)
    stream_key = models.CharField(max_length=50)
    icon_url = models.CharField(max_length=1000)
    icon_redirect_link = models.CharField(max_length=1000, blank=True)
    stream_url = models.CharField(max_length=1000)
    matomo_site_id = models.CharField(max_length=50)
    comments_server = models.CharField(max_length=1000)
    comments_room = models.CharField(max_length=50)
    img_src = models.ImageField(upload_to=fs, blank=True, null=True)
    promote_to_frontpage = models.BooleanField(default=False)
    collect_details = models.BooleanField(default=False)
    facebook_link = models.CharField(max_length=1000, blank=True)
    pleroma_link = models.CharField(max_length=1000, blank=True)
    telegram_link = models.CharField(max_length=1000, blank=True)
    twitter_link = models.CharField(max_length=1000, blank=True)
    youtube_link = models.CharField(max_length=1000, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.stream_key}/{self.title}"



class ContactDetail(models.Model):
    name = models.CharField(max_length=1000)
    mobile_number = PhoneNumberField()
    email_address = models.CharField(max_length=50)
    place = models.CharField(max_length=1000)
    live_stream = models.ForeignKey(LiveStream, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
