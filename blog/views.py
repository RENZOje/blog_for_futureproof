from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *


# Create your views here.

class MainView(ListView):
    model = Post
    template_name = 'main.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tags'] = Tag.objects.all()
        return context


class TagPostView(View):
    def get(self, request, slug):

        tag = Tag.objects.get(link=slug)
        posts = Post.objects.filter(tags=tag)

        context = {'posts' : posts, 'tag': tag}

        return render(request, 'tag_main.html', context)



class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'
    slug_field = 'link'
    context_object_name = 'post'
