from django.shortcuts import render
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})
# Create your views here.
