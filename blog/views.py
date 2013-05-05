from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Blog")


def post_detail_by_index(request, id):
    return HttpResponse("Hello Post by id")


def post_detail(request, slug):
    return HttpResponse("Hello Post by slug")


def category_detail(request, slug):
    return HttpResponse("Hello category by slug")
