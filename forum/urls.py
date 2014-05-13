from django.conf.urls import patterns, include, url
from forum import views

urlpatterns = patterns(
    '',
    url(r'^$', views.main, name='main'),
    url(r'^(?P<id>\d+)/$', views.post, name='post'),
    url(r'^post/(?P<id>\d+)/$', views.reply, name='reply'),    
)

