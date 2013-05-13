from django.conf.urls import patterns, url
from blog.views import PostIndexView, PostDetailViewBySlug, PostDetailViewById


urlpatterns = patterns(
    'blog.views',
    url(r'^$', PostIndexView.as_view()),
    url(r"^(?P<id>[\d+])$", PostDetailViewById.as_view()),
    url(r"^(?P<slug>[-\w]+)/$", PostDetailViewBySlug.as_view(), name="post_detail"),
)
