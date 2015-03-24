from django.http import Http404
from django.utils.translation import ugettext as _
from itertools import chain
from endless_pagination.views import AjaxListView
from django.views.generic import DetailView, ListView
from django.utils import timezone

from blog.models import Post
from projects.models import Project
from taggit.models import TaggedItem, Tag

class PostListView(AjaxListView):
    model = Post
    queryset = Post.objects.published()
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArchiveListView(ListView):
    context_object_name = 'archiveditems'
    template_name = 'archive_list.html'

    def get_queryset(self):
        posts = Post.objects.published()
        projects = Project.objects.published()
        items = sorted(
            chain(posts, projects),
            key=lambda instance: instance.publish,
            reverse=True)
        return items

class PostListViewByTags(AjaxListView):
    context_object_name = 'taggeditems'
    template_name = 'taggeditem_list.html'
    page_template = 'taggeditem_list_page.html'

    def get_queryset(self):
        tag = Tag.objects.get(name=self.args[0])
        items = TaggedItem.objects.filter(tag=tag)
        items = sorted(items, key=lambda x: x.content_object.publish, reverse=True)
        return items

    def get_context_data(self, **kwargs):
        context = super(PostListViewByTags, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        tag = Tag.objects.get(name__in=[self.args[0]])
        context['tag'] = tag
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context


