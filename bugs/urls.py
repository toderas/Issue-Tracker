from django.conf.urls import url, include
from .views import get_bugs, add_new_bug


urlpatterns = [
    url(r'^$', get_bugs),
    url(r'^add/', add_new_bug, name="add_new_bug"),
]
