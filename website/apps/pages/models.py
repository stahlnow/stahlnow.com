from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    """Page model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
    body = models.TextField(_('body'), )
    script = models.TextField(_('script'), null=True, blank=True)

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        db_table = 'pages_pages'
        ordering = ('title',)

    def __unicode__(self):
        return u'%s' % self.title



