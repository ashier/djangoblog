from django.db import models
from django.template.defaultfilters import slugify


class Page(models.Model):

    """Pages"""

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()
    content = models.TextField()
    is_general = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super(Page, self).save(*args, **kwargs)


class Media(models.Model):

    """Public Media"""

    name = models.CharField(max_length=128, unique=True)
    image = models.ImageField(upload_to='page/%Y/%m/%d/', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "medium"
