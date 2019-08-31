from django.conf.urls import url
from .views import search_bugs, search_in_progress, search_author_bugs, search_pending_review, search_resolved, search_features, search_author_features, search_pending_assesment, search_funding_required, search_funding_complete     


urlpatterns = [
    url(r'^search-bugs/$', search_bugs, name='search-bugs'),
    url(r'^search-pending-review/$', search_pending_review, name='Pending-review'),
    url(r'^search-in-progress/$', search_in_progress, name='in-progress-bugs'),
    url(r'^search-resolved/$', search_resolved, name='Resolved'),
    url(r'^search-author-bugs/$', search_author_bugs, name='author-bugs'),
    url(r'^search-features/$', search_features, name='search-features'),
    url(r'^author-features/$', search_author_features, name='author-features'),
    url(r'^search-pending-assesment/$', search_pending_assesment, name='Pending-assesment'),
    url(r'^search-funding-required/$', search_funding_required, name='Funding-required'),
    url(r'^search-funding-complete/$', search_funding_complete, name='Funding-complete'),
    ]