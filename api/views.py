from rest_framework import viewsets, generics

from api.serializers import ProductSerializer, LessonSerializer, StatisticsSerializer
from lms.models import Product, Lesson, ViewedLesson


class ProductListAPIView(generics.ListAPIView):
    """Product view with details about lessons."""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.filter(students__id=self.request.user.id)
        return queryset


class ProductLessonsAPIView(generics.ListAPIView):
    """View contains lessons for particular product."""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class StatisticsListAPIView(generics.ListAPIView):
    """Statistics view."""
    serializer_class = StatisticsSerializer
    queryset = Product.objects.all()
