from el_pagination.views import AjaxListView
from django.views.generic import DetailView
from django.utils import timezone


from projects.models import Project


class ProjectListView(AjaxListView):
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        return context


