from django.conf.urls import patterns, url
from blog.views import IndexView


urlpatterns = patterns(
    'blog.views',
    url(r'^$', IndexView.as_view()),
    url(r"^(?P<id>[\d+])$", 'post_detail_by_index'),
    url(r"^(?P<slug>[^\.]+)", 'post_detail'),
    url(r"^category/(?P<slug>[^\.]+)", 'category_detail'),
)
