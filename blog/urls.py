from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r"^$", 'index'),
    url(r"^scribble/(?P<id>[\d+])$", 'post_detail_by_index'),
    url(r"^scribble/(?P<slug>[^\.]+)", 'post_detail'),
    url(r"^category/(?P<slug>[^\.]+)", 'category_detail'),
)
