from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    db_table = 'post'
    
    name = models.CharField(
        'Name' ,blank=False,null=False,max_length=20,db_index=True 
    )
    body = models.CharField(
        'Body',blank=False,null=False,max_length=100,db_index=True
    )
    
    created_at = models.DateTimeField(
        'createdtime' , blank=True,auto_now_add=True
    )

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = CloudinaryField('file', resource_type='auto')
    uploaded_at = models.DateTimeField(auto_now_add=True)
