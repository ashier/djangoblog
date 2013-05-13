from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from markdown import markdown


class Project(TimeStampedModel):

    """Projects"""

    TYPE_CHOICES = (
        (1, "Web Application"),
        (2, "Desktop Application"),
        (3, "Mobile Application"),
    )

    title = models.CharField(max_length=128, unique=True)
    sub_title = models.TextField()
    slug = AutoSlugField(_('slug'), populate_from='title')
    markdown_content = models.TextField()
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=128)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    html_content = models.TextField(editable=False)
    medium = models.ManyToManyField("Media")
    categories = models.ManyToManyField("Category", related_name='categories', null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', None, {'slug': self.slug})

    def save(self, *args, **kwargs):
        self.html_content = markdown(self.markdown_content)
        super(Project, self).save(*args, **kwargs)


class Media(models.Model):

    """Public Media"""

    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='work/%Y/%m/%d/', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "medium"


class Category(models.Model):

    """Works Category"""

    name = models.CharField(max_length=128, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='title')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
