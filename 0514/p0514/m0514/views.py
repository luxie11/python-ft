from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm

def pagrindinis(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def delete_post(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('pagrindinis')
    else:
        posts = Post.objects.all()
        return render(request, 'posts.html', {'error': "nepavyko istrinti, nes kreipiamasi GET", 'posts': posts})

# Create your views here.
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagrindinis')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})