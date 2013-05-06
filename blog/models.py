from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class Post(TimeStampedModel):
    """Post"""

    title = models.CharField(max_length=128)
    content = HTMLField()
    author = models.ForeignKey(UserFullName, related_name="author")
    slug = AutoSlugField(populate_from='title')
    comments_allowed = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', None, {'slug': self.slug})


class CommentManager(models.Manager):
    def get_query_set(self):
        return super(CommentManager, self).get_query_set().filter(is_spam=False)


class Comment(TimeStampedModel):
    """Post Comments"""

    fullname = models.CharField(max_length=128)
    email = models.CharField(max_length=128, blank=True)
    message = models.TextField(blank=True)
    website = models.URLField(blank=True, null=True)
    post = models.ForeignKey(Post, related_name="comments")
    is_spam = models.BooleanField(default=False)

    objects = CommentManager()

    def __unicode__(self):
        return self.fullname

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = "comments"


class Page(models.Model):
    """Pages"""

    name = models.CharField(max_length=128, unique=True)
    slug = AutoSlugField(populate_from='name')
    content = HTMLField()

    def __unicode__(self):
        return self.fullname


class Category(models.Model):
    """Post Category"""

    name = models.CharField(max_length=128, unique=True)
    slug = AutoSlugField(populate_from='name')
    post = models.ManyToManyField(Post, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
