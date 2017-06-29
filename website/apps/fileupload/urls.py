# encoding: utf-8
from django.conf.urls import url
from fileupload.views import FileCreateView, FileDeleteView, FileListView

urlpatterns = [
    url(r'^new', FileCreateView.as_view(), name='upload-new'),
    url(r'^delete/(?P<pk>\d+)', FileDeleteView.as_view(), name='upload-delete'),
    url(r'^view', FileListView.as_view(), name='upload-view'),
]
