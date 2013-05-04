from django.conf.urls import patterns, include, url
from api.user_resource import UserResource
from tastypie.api import Api


from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v0.1')
v1_api.register(UserResource())


urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
