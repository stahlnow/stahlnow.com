from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from tastypie.api import Api
# from uploader.api import FileResource

from projects.views import ProjectListView
from blog.views import PostListViewByTags, ArchiveListView


admin.autodiscover()

# v1_api = Api(api_name=settings.API_VERSION)     # settings.API_VERSION = 'v1'
# v1_api.register(FileResource())


urlpatterns = [

    url(r'^$', ProjectListView.as_view(), name='projects'),

    url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),

    url(r'^show/([\w-]+)', PostListViewByTags.as_view()),
    url(r'^archive/', ArchiveListView.as_view()),

    url(r'^upload/', include('fileupload.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('pages.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
