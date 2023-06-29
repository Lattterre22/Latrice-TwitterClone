from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import  redirect
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or desired URL
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})



def index(request):
    #If the method is POST
    form= PostForm(request.POST)
    if request.method =='POST':   
        #If the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            #No, Show Error
            return HttpResponseRedirect("form.errors.as_json()")
    #Get all posts, limit = 20 
    posts= Post.objects.all().order_by('-created_at')[:20]

    #Show
    return render(request,'posts.html', {'posts':posts})




def delete(request,post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    output='POST ID s'+ str (post_id)
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm(instance=post)

    return render(request, 'edit.html', {'form': form, 'post_id': post_id})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or desired URL
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})