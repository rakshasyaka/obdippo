from django.conf.urls import url

from . import views as v

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^entry/(?P<pk>[0-9]+)/?', v.detail_entry, name='detail_entry'),
    url(
        r'^category/(?P<cat_name>[a-z,_]+)/?',
        v.entries_in_cat, name='en_for_single_cat'
    ),
]
