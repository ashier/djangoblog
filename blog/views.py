from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "blog/main.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


def post_detail_by_index(request, id):
    return HttpResponse("Hello Post by id")


def post_detail(request, slug):
    return HttpResponse("Hello Post by slug")
