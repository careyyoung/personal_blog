# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

class time_stamped_model(models.Model):
    """
    abstract base class, 提供创建时间和修改时间两个通用的field
    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
#class test(time_stamped_model): #继承abstract base class:time_stamped_model,test表就有上面通用的field
#    test1 = models.CharField(max_length=200)


class Category(time_stamped_model):
    category_name = models.CharField(max_length=200,verbose_name="分类名称")
    category_description = models.CharField(max_length=200,verbose_name="分类描述")
    
    def __unicode__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
        ordering=['modified_time']  # 升序排列
        db_table = "category" 


class Blog(time_stamped_model):
    title = models.CharField(max_length=200,verbose_name="标题")
    description = models.CharField(max_length=200,blank=True,verbose_name="描述")
    content = models.TextField(verbose_name="内容")
    author = models.CharField(max_length=200,verbose_name="作者")
    category = models.ForeignKey(Category)
    views = models.IntegerField(default=0,verbose_name="浏览数")
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"
        ordering=['modified_time']  # 升序排列
        db_table = "blog"     


class Profile(time_stamped_model):
    nick_name = models.CharField(max_length=200,verbose_name="昵称")
    picture = models.CharField(max_length=200,blank=True,verbose_name="头像")
    email = models.EmailField(blank=True,verbose_name="邮箱")
    location = models.CharField(max_length=200,blank=True,verbose_name="位置")
    qq = models.IntegerField(null=True,verbose_name="QQ")
    weibo = models.CharField(max_length=200,blank=True,verbose_name="微博")
    job = models.CharField(max_length=200,blank=True,verbose_name="工作")
    
    def __unicode__(self):
        return self.nick_name

    class Meta:
        verbose_name = "个人资料"
        verbose_name_plural = "个人资料"
        ordering=['modified_time']  # 升序排列
        db_table = "profile" 



#message: message_id/name/email/content/
class Message(time_stamped_model):
    name = models.CharField(max_length=20,verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    content = models.CharField(max_length=250,verbose_name="内容")
    
    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = "留言"
        verbose_name_plural = "留言"
        ordering=['modified_time']  # 升序排列
        db_table = "message" 


class Comment(time_stamped_model):
    blog = models.ForeignKey(Blog)
    name = models.CharField(max_length=20,verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    content = models.CharField(max_length=250,verbose_name="内容")
    
    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        ordering=['modified_time']  # 升序排列
        db_table = "comment"

