from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.get(text = "rubychen")
    return render(request, 'polls/post_list.html', {'posts': posts})
