from django.conf.urls import url
from django_slug_app import views

urlpatterns = [ 
	url(r'^$', views.Index.as_view(), name = 'post'),
	url(r'^post/$', views.PostView.as_view(), name = 'post'),
    url(r'^list/$', views.PostListView.as_view(), name = 'list'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post-detail'),
]
