from django.shortcuts import render,get_object_or_404
from . import models

def all_blog(request):
    blogs = models.Blog.objects.all()
    return render(request,'blog/all_blog.html', {'blogs' : blogs})

def detail(request,blog_id):
    blog=get_object_or_404(models.Blog,pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
