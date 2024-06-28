from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    return render(request, 'blog/post/list.html', {
        'posts': Post.published.all()
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {
        'post': post
    })
