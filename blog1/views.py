# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from blog1.models import Blog, Message
from blog1.serializers import BlogSerializer, MessageSerializer

# Create your views here.

# hello just for testing. 
#1. goto common.py, "'blog1'," appended to INSTALLED_APPS next line 33.
#2. goto hello_app.html, change line 3 to the correct name
#3. goto urls.py, change line 12 to the correct name
#4. access http://127.0.0.1:9999/blog1/hello
def hello(request):
    return render(request, 'blog1/hello_app.html')

# Create your views here.
def index(request):
    return render(request, 'blog1/index.html')


def blogs(request):
    blogs_list = Blog.objects.all()
    
    return render(request, 'blog1/blogs.html', {'blogs_list':blogs_list})

def detail(request, blog_id=''):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'blog1/detail.html', {'blog':blog})

def about(request):
    return render(request, 'blog1/about.html')


class BlogViewSet(viewsets.ModelViewSet):
    """
            允许查看和编辑Blog 的 API endpoint
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
            允许查看和编辑 Message 的 API endpoint
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



