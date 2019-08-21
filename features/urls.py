from django.conf.urls import url, include
from .views import all_features, add_new_feature, get_current_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^add-feature/', add_new_feature, name="add_new_feature"),
    url(r'^get-feature/(?P<id>\d+)', get_current_feature, name="get-feature"),
]