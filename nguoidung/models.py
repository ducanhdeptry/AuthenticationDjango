from django.db import models
from xacthuc.settings import *
from django.conf.urls.static import static
from django.conf import settings

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(
        null=False, auto_created=True, primary_key=True
    )
    title = models.CharField(max_length=255)
    shortDesc = models.TextField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    imgUrl = models.ImageField(
        upload_to=settings.MEDIA_ROOT, blank=True, default='1109355.jpg')
