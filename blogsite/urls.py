from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/$', views.post, name='post'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/tag/(?P<tag>\w+)/$', views.post_tags, name='post_tags'),
	url(r'^post/user/(?P<user>\w+)/$', views.post_author, name='post_author'),
	url(r'^register/$', views.register, name='register'),
]