# Imports {{{
from PIL import Image as PImage

from aakashlabs.settings import MEDIA_URL
from forum.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    context = RequestContext(request)
    categories = Category.objects.all()

    print categories
    context_dict = {
        'categories': categories,
    }
    return render_to_response('forum/main.html', context_dict, context)

def post(request, id):
    context = RequestContext(request)
    category = Category.objects.get(pk=id)
    posts = Post.objects.filter(category=category)

    context_dict = {
        'posts': posts,
    }
    
    return render_to_response("forum/post.html", context_dict, context)


def reply(request, id):
    context = RequestContext(request)
    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(title=post)

    context_dict = {
        'post': post,
        'replies': replies,
    }
    
    return render_to_response("forum/reply.html", context_dict, context)
