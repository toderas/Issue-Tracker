from django.conf.urls import url, include
from .views import get_bugs, add_new_bug, get_current_bug, remove_comment, add_upvotes, delete_bug, edit_bug
from django.views import static
from master.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^current-bugs/$', get_bugs, name="show_bugs"),
    url(r'^add-bug/', add_new_bug, name="add_new_bug"),
    url(r'^get-bug/(?P<id>\d+)', get_current_bug, name="get-bug"),
    url(r'^remove-comment/(\d+)/$', remove_comment, name="delete-comment"),
    url(r'^add-upvote/(?P<id>\d+)', add_upvotes, name="add-upvote"),
    url(r'^delete-bug/(\d+)/$', delete_bug, name="delete-bug"),
    url(r'^edit-bug/(?P<id>\d+)', edit_bug, name="edit-bug"),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
