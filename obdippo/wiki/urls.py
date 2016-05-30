from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
    r'^(?P<cat_name>[a-z,_]+)/?', views.entries_in_cat, name='en_for_single_cat'
    ),
]
