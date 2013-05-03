from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User


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


class Reply(TimeStampedModel):
    """Post Comments"""

    fullname = models.CharField(max_length=128)
    email = models.CharField(max_length=128, blank=True)
    message = models.TextField(blank=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.fullname


class Post(TimeStampedModel):
    """Post"""

    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(User)
    permalink = models.URLField(blank=True)
    categories = models.ManyToManyField(Category)
    replies = models.ManyToManyField(Reply, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('created',)
