# encoding: utf-8
from django.conf.urls import url
from uploader.views import FileListView
from uploader.views import FileCreateView


urlpatterns = [
    url(r'^$', FileListView.as_view(), name='list'),
]
