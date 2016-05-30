from django.shortcuts import render, HttpResponse
from .models import Category, Entry, Comment


def index(request):
    all_categories = Category.objects.all()
    output = '<br/>'.join([c.name for c in all_categories])
    return HttpResponse(output)


# TODO: related request Глупо искать по всем записям без уточнений!
# select_related видимо не работает для ManyToManyField

def entries_in_cat(request, cat_name):
    all_entries = Entry.objects.filter(category__name=cat_name).prefetch_related('category')
    context = {
        'cat_name': cat_name,
        'all_entries': all_entries
    }
    return render(request, 'wiki/sinCatEnt.html', context)
