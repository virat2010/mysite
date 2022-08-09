from django.conf.urls import *
from django.urls import *
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'post/(?P<pk>\d+)$',views.PostDetalView.as_view(),name='post_detail'),
    url(r'post/new/$',views.CreatePostView.as_view(),name='post_name'),
    url(r'post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
]
