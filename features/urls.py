from django.conf.urls import url, include
from .views import all_features, add_new_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^add-feature/', add_new_feature, name="add_new_feature"),
]