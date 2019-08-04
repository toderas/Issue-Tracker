from django.conf.urls import url
from .views import search_bugs

urlpatterns = [
#    url(r'^$', do_search, name='search'),
    url(r'^search-bugs/$', search_bugs, name='search-bugs'),
    ]