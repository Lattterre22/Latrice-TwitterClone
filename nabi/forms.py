from django import forms
from .models import Post
from .models import UploadedFile

class PostForm(forms.ModelForm):
    class Meta:
        model= Post 
        fields='__all__'
        

class TweetForm(forms.Form):
    text = forms.CharField(label='Text', max_length=280)
    image = forms.ImageField(label='Image', required=False)



class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)  # Add any additional fields if needed
