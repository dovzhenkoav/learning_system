from rest_framework import viewsets, generics

from api.serializers import ProductSerializer, LessonSerializer
from lms.models import Product, Lesson, ViewedLesson


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    def get_queryset(self):
        queryset = Product.objects.filter(students__id=self.request.user.id)
        return queryset


class ProductLessonsAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

