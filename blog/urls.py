from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r"^$", 'index'),
    url(r"^post/(?P<id>[\d+])$", 'post_detail_by_index'),
    url(r"^post/(?P<slug>[^\.]+)", 'post_detail'),
    url(r"^category/(?P<slug>[^\.]+)", 'category_detail'),
)
