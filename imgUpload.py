__author__ = 'travisselland'
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basetemp.settings")
from django.contrib.auth.models import User

import django
django.setup()

from gallery import models as mod

try:
  User.objects.get(username='tselland')
except User.DoesNotExist:
  u = User()
  u.username = 'tselland' # change the username whatever you like
  u.set_password('test') # change the password whatever you like
  u.first_name = 'Travis'
  u.last_name = 'Selland'
  u.email = 't@s.com'
  u.is_superuser = True
  u.is_staff = True
  u.save()


try:
  mod.databaseImage.objects.get(fileName='image_1.jpg')
except mod.databaseImage.DoesNotExist:
  img = mod.databaseImage()
  img.fileName = "image_1.jpg"
  img.mime_type = "image/jpg"
  img.filePath = "/gallery/images/"
  img.imgTitle = "Go"
  img.save()

try:
  mod.databaseImage.objects.get(fileName='image_2.jpg')
except mod.databaseImage.DoesNotExist:
  img = mod.databaseImage()
  img.fileName = "image_2.jpg"
  img.mime_type = "image/jpg"
  img.filePath = "/gallery/images/"
  img.imgTitle = "Pro"
  img.save()

try:
  mod.databaseImage.objects.get(fileName='image_3.jpg')
except mod.databaseImage.DoesNotExist:
  img = mod.databaseImage()
  img.fileName = "image_3.jpg"
  img.mime_type = "image/jpg"
  img.filePath = "/gallery/images/"
  img.imgTitle = "OR"
  img.save()

try:
  mod.databaseImage.objects.get(fileName='image_4.jpg')
except mod.databaseImage.DoesNotExist:
  img = mod.databaseImage()
  img.fileName = "image_4.jpeg"
  img.mime_type = "image/jpeg"
  img.filePath = "/gallery/images/"
  img.imgTitle = "Go"
  img.save()

try:
  mod.databaseImage.objects.get(fileName='image_5.jpg')
except mod.databaseImage.DoesNotExist:
  img = mod.databaseImage()
  img.fileName = "image_5.jpg"
  img.mime_type = "image/jpg"
  img.filePath = "/gallery/images/"
  img.imgTitle = "Home"
  img.save()