from django.contrib import admin
from .models import Post 
from .models import UploadedFile

admin.site.register(Post) 

admin.site.register(UploadedFile)