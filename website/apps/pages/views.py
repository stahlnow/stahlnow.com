from django.views.generic import DetailView

from pages.models import Page

class PageDetailView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        return context


