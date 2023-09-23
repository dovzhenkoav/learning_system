from django.views import generic

from lms.models import Product, Lesson, ViewedLesson


class ProductListView(generic.ListView):
    model = Product
    template_name = 'lms/index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(students__id=self.request.user.id)
        return queryset
