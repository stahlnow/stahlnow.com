from django.conf.urls import patterns, url
from pages.views import PageDetailView

urlpatterns = patterns('pages.views',
                       url(r'(?P<slug>[-_\w]+)/$', PageDetailView.as_view(), name='page_detail'),
)