from django.conf.urls import patterns, url
from pages.views import IndexView, AboutView


urlpatterns = patterns(
    'pages.views',
    url(r'^$', IndexView.as_view()),
    url(r'^about/$', AboutView.as_view()),
)
