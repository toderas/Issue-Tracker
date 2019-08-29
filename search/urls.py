from django.conf.urls import url
from .views import search_bugs, search_in_progress, search_author_bugs, search_pending_review, search_resolved, search_features

urlpatterns = [
    url(r'^search-bugs/$', search_bugs, name='search-bugs'),
    url(r'^search-pending-review/$', search_pending_review, name='Pending-review'),
    url(r'^search-in-progress/$', search_in_progress, name='in-progress-bugs'),
    url(r'^search-resolved/$', search_resolved, name='Resolved'),
    url(r'^search-author-bugs/$', search_author_bugs, name='author-bugs'),
    url(r'^search-features/$', search_features, name='search-features'),
    ]