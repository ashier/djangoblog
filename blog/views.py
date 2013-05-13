from django.views.generic import TemplateView


class PostIndexView(TemplateView):
    template_name = "blog/main.html"

    def get_context_data(self, **kwargs):
        context = super(PostIndexView, self).get_context_data(**kwargs)
        return context


class PostDetailViewById(TemplateView):
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailViewById, self).get_context_data(**kwargs)
        return context


class PostDetailViewBySlug(TemplateView):
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailViewBySlug, self).get_context_data(**kwargs)
        return context
