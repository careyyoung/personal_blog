# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import Category,Blog,Profile,Message,Comment

# Register your models here.
# So you can see this model in admin page
#admin.site.register(model_name)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Comment)
