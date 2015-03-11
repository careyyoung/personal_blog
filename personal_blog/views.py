# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'personal_blog/hello_project.html')
