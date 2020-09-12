from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.forms import inlineformset_factory
from django.utils import timezone

# Create your views here.

class MainView(ListView):
    model = Post
    template_name = 'main.html'
    queryset = Post.objects.filter(draft=False)
    context_object_name = 'posts'
    ordering = ['-time_creation']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class DraftPostView(ListView):
    model = Post
    template_name = 'main.html'
    queryset = Post.objects.filter(draft=True)
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class TagPostView(View):
    def get(self, request, slug):
        tag = Tag.objects.get(link=slug)
        posts = Post.objects.filter(tags=tag, draft=False)

        context = {'posts': posts, 'tag': tag}

        return render(request, 'tag_main.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'
    slug_field = 'link'
    context_object_name = 'post'




def create_tag(request):

    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/post_form.html', context)

def delete_tag(request, pk):
    post = Tag.objects.get(id=pk)
    if request.method == "GET":
        post.delete()
        return redirect('/')



def create_post(request, pk):
    author = Author.objects.get(id=pk)

    form = PostForm(initial={'author': author})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/post_form.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    state_draft = post.draft
    if state_draft:
        print(state_draft)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.cleaned_data['time_last_update'] = timezone.now()
            form.save()
            return redirect('/')

    context = { 'form': form }
    return render(request, 'accounts/post_form.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "GET":
        post.delete()
        return redirect('/')



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
