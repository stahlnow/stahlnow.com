from django.conf.urls import patterns, url
from blog.views import PostListView, PostListViewByTags, PostDetailView

urlpatterns = patterns(
    'blog.views',
    url(r'^$', PostListView.as_view(), name='home'),
    url(r'^(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post_detail')
)
