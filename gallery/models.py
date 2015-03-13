from django.db import models
from django.conf import settings
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class databaseImage(models.Model):

    mime_types = (
        ( 'image/gif', 'gif' ),
        ( 'image/jpeg', 'jpeg' ),
        ( 'image/pjpeg', 'pjpeg' ),
        ( 'image/gif', 'gif' ),
        ( 'image/tiff', 'tiff' ),
    )

    fileName = models.TextField(max_length=100)
    mime_type = models.TextField(max_length=20)
    filePath = models.TextField(max_length=50)
    imgTitle = models.TextField(max_length=15)

    def __str__(self):
        return str(self.fileName)

    def to_html(self):
        return format_html(('<img src="{0}{1}" data-title="{2}" alt="{1}"/>'.format( settings.MEDIA_URL, self.fileName, self.imgTitle)))

