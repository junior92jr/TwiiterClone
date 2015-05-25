from django.conf.urls import patterns, url
from twitterclone import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add_tweet/$', views.add_tweet, name='add_tweet'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
)