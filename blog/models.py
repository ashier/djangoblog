from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserFullName(User):

    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class Post(TimeStampedModel):

    """Post"""

    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(UserFullName, related_name="author")
    slug = models.SlugField()
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
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):

    """Post Category"""

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super(Category, self).save(*args, **kwargs)


class Media(models.Model):

    """Public Media"""

    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='post/%Y/%m/%d/', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "medium"
