from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=500, unique=True)
    link = models.SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.link = slugify(self.title)

        super(Tag, self).save()

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
    image = models.ImageField(blank=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    time_publish = models.DateTimeField(auto_now=True, null=True)
    time_last_update = models.DateTimeField(auto_now=True,null=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    link = models.SlugField(unique=True)
    draft = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.link = slugify(self.title)

        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'slug': self.link})

    class Meta:
        ordering = ['time_creation']

    def __str__(self):
        return self.title
