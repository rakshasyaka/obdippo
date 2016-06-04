from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.SlugField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(blank=True)
    category = models.ManyToManyField(Category)
    # Can add functional of estimate "question" state
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(safe):
        return Httpreverse('detail_entry', kwargs={'pk': self.pk})


class Comment(models.Model):
    person = models.CharField(max_length=255, verbose_name="who's comment")
    publish = models.DateTimeField(auto_now_add=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    title = models.SlugField(blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title
