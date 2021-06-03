from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request , 'index.html' , context = {'posts':posts})

def post(request , pk):
    posts = Post.objects.get(id = pk)
    return render(request ,'post.html',context = {'posts':posts})
