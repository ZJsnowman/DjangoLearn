from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<article_id>[0-9]+)/$', views.get_detail, name='detail'),
    url(r'^create/(?P<article_id>[0-9]+)/$', views.create_or_edit, name='create'),
    url(r'^action_create/$', views.action_create, name='action_create'),

]
