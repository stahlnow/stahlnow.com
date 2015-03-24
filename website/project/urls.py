from django.conf.urls import patterns, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from tastypie.api import Api
from uploader.api import FileResource

from blog.views import PostListViewByTags, ArchiveListView

admin.autodiscover()

v1_api = Api(api_name=settings.API_VERSION)     # settings.API_VERSION = 'v1'
v1_api.register(FileResource())


urlpatterns = patterns(
    '',
    (r'^$', include('blog.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^projects/', include('projects.urls')),

    (r'^show/([\w-]+)/$', PostListViewByTags.as_view()),
    (r'^archive/$', ArchiveListView.as_view()),

    (r'^upload/', include('fileupload.urls')),
    (r'^uploader/', include('uploader.urls')),

    (r'^api/', include(v1_api.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),

    (r'^admin/', include(admin.site.urls)),

    (r'^', include('pages.urls')),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
