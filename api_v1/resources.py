from blog.models import Post, Category
from works.models import Project

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class WorkResource(ModelResource):

    class Meta:
        queryset = Project.objects.all()
        allowed_methods = ['get']
        authentication = MultiAuthentication(
            BasicAuthentication(), ApiKeyAuthentication())

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"


class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all()
        allowed_methods = ['get']
        resource_name = 'category'
        authentication = MultiAuthentication(
            BasicAuthentication(), ApiKeyAuthentication())
        filtering = {
            "slug": ('exact', 'startswith',),
            "name": ALL,
        }

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"


class PostResource(ModelResource):

    categories = fields.ToManyField(CategoryResource, 'categories', full=True)

    class Meta:
        queryset = Post.objects.all()
        list_allowed_methods = ['get']
        excludes = ['modified', 'markdown_content']
        resource_name = 'note'
        authentication = MultiAuthentication(
            BasicAuthentication(), ApiKeyAuthentication())
        filtering = {
            "slug": ('exact', 'startswith',),
            'categories': ALL_WITH_RELATIONS,
            "title": ALL,
        }

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"

    # def dehydrate_created(self, bundle):
    #     return bundle.data['created'].strftime("%B %d, %Y")
