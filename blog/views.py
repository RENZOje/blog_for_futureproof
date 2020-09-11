from django.shortcuts import render
from .models import *


# Create your views here.
def home_page(request):

    posts = Post.objects.all()
    tags = Tag.objects.all()

    context = {'posts': posts,
               'tags':tags
               }

    return render(request, 'index.html', context)