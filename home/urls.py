from django.conf.urls import patterns, url
from home.views import IndexView


urlpatterns = patterns(
    'home.views',
    url(r'^$', IndexView.as_view()),
)
