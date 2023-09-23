from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import generic

from lms.models import Product, Lesson, ViewedLesson
from lms.services import open_file


class ProductListView(generic.ListView):
    model = Product
    template_name = 'lms/index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(students__id=self.request.user.id)
        return queryset


class LessonsListView(generic.ListView):
    model = Lesson
    template_name = 'lms/lessons.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        pk = self.kwargs.get('pk')
        queryset = Lesson.objects.filter(product_id=pk)

        return queryset


def lesson_detail(request, pk: int):
    obj = Lesson.objects.get(pk=pk)
    return render(request, "lms/lesson-detail.html", {"object": obj})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


