from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    # image = models.ImageField(blank=True)
    # author =
    # time_publication = models.TimeField(auto_now=True)
    time_creation = models.TimeField(auto_now=True)
    link = models.SlugField(unique=True)
    draft = models.BooleanField()
    publish = models.BooleanField()

    class Meta:
        ordering = ['time_creation']

    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=500, unique=True)
    link = models.SlugField(unique=True)
    posts = models.ManyToManyField(Post,)

    def __str__(self):
        return self.title