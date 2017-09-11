# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template
# Create your views here

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
'''    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + unicode(str(post),'utf-8') +"<br>")
        post_lists.append("<small>" + unicode(str(post.body.encode('utf-8')),'utf-8') +"</small><br><br>")
'''
