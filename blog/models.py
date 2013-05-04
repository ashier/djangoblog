from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class Category(models.Model):
    """Post Category"""

    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"


class Reply(TimeStampedModel):
    """Post Comments"""

    fullname = models.CharField(max_length=128)
    email = models.CharField(max_length=128, blank=True)
    message = models.TextField(blank=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "Replies"


class Post(TimeStampedModel):
    """Post"""

    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(UserFullName, related_name="posts")
    categories = models.ManyToManyField(Category)
    slug = AutoSlugField(populate_from='title')
    replies = models.ManyToManyField(Reply, blank=True)
    reply_enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', None, { 'slug': self.slug })
