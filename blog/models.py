from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=500, unique=True)
    link = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('detail_tag', kwargs={'slug': self.link})

    def __str__(self):
        return self.title



class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


    def __str__(self):
        return f'{self.user.username}'


class Post(models.Model):
    title = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    # time_publication = models.TimeField(auto_now=True)
    time_creation = models.DateTimeField(auto_now=True)
    link = models.SlugField(unique=True)
    draft = models.BooleanField()
    publish = models.BooleanField()
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'slug': self.link})

    class Meta:
        ordering = ['time_creation']

    def __str__(self):
        return self.title
