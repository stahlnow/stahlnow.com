from django.conf.urls import url
from projects.views import ProjectListView, ProjectDetailView

urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='projects'),
    url(r'^(?P<slug>[-_\w]+)/$', ProjectDetailView.as_view(), name='project_detail'),

]