from django.conf.urls import url, include
from .views import get_bugs, add_new_bug


urlpatterns = [
    url(r'^current-bugs/$', get_bugs, name="show_bugs"),
    url(r'^add-bug/', add_new_bug, name="add_new_bug"),
]
