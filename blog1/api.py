# -*- coding: UTF-8 -*-
'''
Created on 2015年3月12日

@author: carey.yang
'''
from rest_framework import generics, permissions

from serializers import BlogSerializer, MessageSerializer
from models import Blog, Message

class BlogList(generics.ListCreateAPIView):
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = 'id'
    permission_classes = [
        permissions.AllowAny
        ]
    queryset = Blog.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MessageList(generics.ListCreateAPIView):
    model = Message
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Message
    serializer_class = MessageSerializer
    lookup_field = 'id'
    permission_classes = [
        permissions.AllowAny
        ]
    queryset = Message.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

