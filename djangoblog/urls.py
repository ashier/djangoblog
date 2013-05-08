from django.conf.urls import patterns, include, url
from api_v1.resources import PostResource, CategoryResource, CommentResource
from tastypie.api import Api


from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(PostResource())
v1_api.register(CategoryResource())
v1_api.register(CommentResource())


urlpatterns = patterns(
    '',
    # urls below
    url(r'^$', include('home.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/'}),
    url(r'^notes/', include('blog.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
