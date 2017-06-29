from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.conf import settings

from projects.managers import PublicManager

from taggit.managers import TaggableManager

from fileupload.models import File

class Category(models.Model):
    """Category model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'project_categories'
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title


class Project(models.Model):
    """Project model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey(User)
    body = models.TextField(_('body'), )
    teaser = models.ForeignKey(File, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)
    publish = models.DateTimeField(_('publish'), default=now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    category = models.ForeignKey(Category, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tags = TaggableManager()
    objects = PublicManager()

    def image_tag(self):
        return u'<img src="%s" width="400px" />' % (settings.FILES_URL + self.teaser.file.url)

    image_tag.short_description = 'Teaser'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        db_table = 'project_projects'
        ordering = ('my_order',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'project_detail', (), {'slug': self.slug}

    def get_next(self):
        next = Project.objects.filter(my_order__gt=self.my_order)
        if next:
            return next.first().get_absolute_url()
        return Project.objects.get(my_order=1).get_absolute_url()

    def get_previous(self):
        prev = Project.objects.filter(my_order__lt=self.my_order).order_by('-my_order')
        if prev:
            return prev.first().get_absolute_url()
        return Project.objects.order_by('-my_order')[0].get_absolute_url()


