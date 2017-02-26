from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/flight=(?P<flight_id>[0-9]+)&departure=(?P<departure>[A-Za-z]+)&arrival=(?P<arrival>[A-Za-z]+)&airline=(?P<airline>[A-Za-z]+)/$', views.search, name='search'),
]
# url(r'^c/(?P<class_id>\d+)/$', 'App.views.view_single_class', name='class_view'),
