from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# POSTS VIEW ENDPOINT
def posts(request):
    queryset = Post.objects.all()
    context = {
        "posts" : queryset
    }
    return render(request, 'posts/blog-listing.html',context)


# POST DETAILS VIEW ENDPOINT
def post_details(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/blog-post.html',context)
