# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from blog1.api import BlogList, BlogDetail, MessageList, MessageDetail
from blog1.views import BlogViewSet, MessageViewSet


# api.py 的方法
blog_urls = patterns('',  
    url(r'^$', BlogList.as_view(), name='blog-list'),  
    url(r'^(?P<id>\d+)/$', BlogDetail.as_view(), name='blog-detail'),  
) 

message_urls = patterns('',  
    url(r'^$', MessageList.as_view(), name='message-list'),  
    url(r'^(?P<id>\d+)/$', MessageDetail.as_view(), name='message-detail'),  
) 


'''
# veiwset 的方法
message_list = MessageViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })

message_detail = MessageViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })
'''

router = DefaultRouter()
router.register(r'message', MessageViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'personal_blog.views.hello',),
    url(r'^blog1/hello/$', 'blog1.views.hello',),
    url(r'^blog1/index/$', 'blog1.views.index', name='index'),
    url(r'^blog1/blogs/$', 'blog1.views.blogs', name='blogs'),
    url(r'^blog1/detail/(?P<blog_id>\d+)/$', 'blog1.views.detail', name='detail'),
    url(r'^blog1/about/$', 'blog1.views.about', name='about'),
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # api 的url配置
    url(r'^blog/', include(blog_urls)),
    url(r'^message1/', include(message_urls)),
    
    # veiwset url 配置
    url(r'^', include(router.urls)),
)

