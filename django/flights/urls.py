from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
]
# url(r'^c/(?P<class_id>\d+)/$', 'App.views.view_single_class', name='class_view'),
