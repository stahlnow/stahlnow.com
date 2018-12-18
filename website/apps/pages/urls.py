from django.conf.urls import url
from pages.views import PageDetailView

urlpatterns = [
    url(r'(?P<slug>[-_\w]+)/$', PageDetailView.as_view(), name='page_detail'),
]