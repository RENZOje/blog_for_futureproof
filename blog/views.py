from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from forms import CreateUserForm
from django.contrib import messages


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


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                user_ins = form.instance
                Author.objects.create(user=user_ins, email=form.cleaned_data.get('email'))

                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')