from django.contrib import admin
from .models import UploadTxt, UploadImage, UploadAudio, UploadVideo

# Register your models here.
admin.site.register(UploadTxt)
admin.site.register(UploadImage)
admin.site.register(UploadAudio)
admin.site.register(UploadVideo)
