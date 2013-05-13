from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from markdown import markdown


class UserFullName(User):

    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class Post(TimeStampedModel):

    """Post"""

    title = models.CharField(max_length=128)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    author = models.ForeignKey(UserFullName, related_name="author")
    slug = AutoSlugField(_('slug'), populate_from='title')
    header_image = models.ImageField(upload_to='post/%Y/%m/%d/', null=True, blank=True)
    categories = models.ManyToManyField("Category", related_name='categories', null=True, blank=True)

    def __unicode__(self):
        return self.title

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

    class Meta:
        ordering = ('-created',)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', None, {'slug': self.slug})

    def save(self, *args, **kwargs):
        self.html_content = markdown(self.markdown_content)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):

    """Post Category"""

    name = models.CharField(max_length=128, unique=True)
    slug = AutoSlugField(_('slug'), populate_from='name')
    posts = models.ManyToManyField("Post", related_name='posts', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


class Media(models.Model):

    """Public Media"""

    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='post/%Y/%m/%d/', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "medium"
