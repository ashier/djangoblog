from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):

    """Projects"""

    title = models.CharField(max_length=128, unique=True)
    sub_title = models.TextField()
    slug = models.SlugField()
    content = models.TextField()
    medium = models.ManyToManyField("Media")
    categories = models.ManyToManyField("Category", related_name='categories', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
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
