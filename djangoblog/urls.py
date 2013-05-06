from django.conf.urls import patterns, include, url
from api_v10.resources import PostResource, CategoryResource, CommentResource
from tastypie.api import Api


from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1.0')
v1_api.register(PostResource())
v1_api.register(CategoryResource())
v1_api.register(CommentResource())


urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^blog/', include('blog.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
