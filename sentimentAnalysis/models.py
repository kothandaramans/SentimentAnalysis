from django.db import models

# Create your models here.

class UploadTxt(models.Model):
    text = models.FileField(upload_to='txt')

class UploadImage(models.Model):
    image = models.ImageField(upload_to='images')

class UploadAudio(models.Model):
    audio = models.FileField(upload_to='audio')

class UploadVideo(models.Model):
    video = models.FileField(upload_to='video')
