# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

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
    
    
)
