from django.shortcuts import render
from .models import Post

def allBlogs(request):
    allPosts= Post.objects.all()
    print(allPosts)
    context={'allPosts': allPosts}
    context['secondPosts'] = [i for i in range(10)]
    print(context)
    return render(request,'blog/all_blogs.html',context)


