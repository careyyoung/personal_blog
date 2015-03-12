# -*- coding: UTF-8 -*-
'''
Created on 2015年3月12日

@author: carey.yang
'''
from models import Blog, Category, Message
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_description', 'created_time', 'modified_time')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(required=True)  
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'content', 'author','category', 'views', 'created_time', 'modified_time')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'name', 'email', 'content', 'created_time', 'modified_time')

