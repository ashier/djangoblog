from tastypie.resources import ModelResource
from tastypie import fields
from blog.models import Post, Comment, Category
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.constants import ALL


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        allowed_methods = ['get']
        excludes = ['modified', 'is_spam']
        resource_name = 'comment'
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"


class PostResource(ModelResource):
    comments = fields.ToManyField(CommentResource, 'comments', null=True, full=True)

    class Meta:
        queryset = Post.objects.all()
        list_allowed_methods = ['get']
        excludes = ['modified']
        resource_name = 'post'
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        filtering = {
            "slug": ('exact', 'startswith',),
            "title": ALL,
        }

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"

    # def dehydrate_created(self, bundle):
    #     return bundle.data['created'].strftime("%B %d, %Y")


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        allowed_methods = ['get']
        resource_name = 'category'
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        filtering = {
            "slug": ('exact', 'startswith',),
            "name": ALL,
        }

    def determine_format(self, request):
        """ Automatic accept header to JSON format """
        return "application/json"
