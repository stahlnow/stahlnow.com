from django.conf.urls import patterns, url
from projects.views import ProjectListView, ProjectDetailView

urlpatterns = patterns('projects.views',
                       url(r'^$', ProjectListView.as_view(), name='projects'),
                       url(r'^(?P<slug>[-_\w]+)/$', ProjectDetailView.as_view(), name='project_detail'),

)