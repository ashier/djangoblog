from django.conf.urls import patterns, url
from works.views import IndexView


urlpatterns = patterns(
    'works.views',
    url(r'^$', IndexView.as_view()),
)
