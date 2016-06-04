from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .models import Category, Entry, Comment


def index(request):
    # ПЛОХО! TODO: не выбирать из базы все записи,
    # что бы потом выбрать последние 5
    latest_pk = Entry.objects.latest('pk').pk
    if latest_pk >= 4:
        three_entry = Entry.objects.filter(
            pk__gte=(latest_pk - 3)
        )
    else:
        three_entry = Entry.objects.filter(
            pk__gte=1
        )
    all_categories = Category.objects.all()
    context = {
        'three_entry': three_entry,
        'all_categories': all_categories,
    }
    return render(request, 'wiki/index.html', context)


# TODO: related request Глупо искать по всем записям без уточнений!
# select_related видимо не работает для ManyToManyField

def entries_in_cat(request, cat_name):
    all_entries = Entry.objects.filter(
        category__name=cat_name).prefetch_related('category')
    context = {
        'cat_name': cat_name,
        'all_entries': all_entries
    }
    return render(request, 'wiki/sinCatEnt.html', context)


def detail_entry(request, pk=None):
    if pk is None:
        single_entry = "Еще нет записи"
    else:
        single_entry = Entry.objects.filter(pk=pk)
    context = {
        'single_entry': single_entry
    }
    return render(request, 'wiki/singleEntry.html', context)



class EntryCreate(CreateView):
    model = Entry
    fields = ['title', 'text', 'image', 'category']
