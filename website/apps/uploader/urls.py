# encoding: utf-8
from django.conf.urls import patterns, url
from uploader.views import FileListView
from uploader.views import FileCreateView


urlpatterns = patterns('',
                       url(r'^$', FileListView.as_view(), name='list'),
                       )
