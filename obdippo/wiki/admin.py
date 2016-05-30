from django.contrib import admin
from .models import Category, Entry, Comment

admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Comment)
