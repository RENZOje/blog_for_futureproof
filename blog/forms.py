from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','description','image','draft','tags']


class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['title']