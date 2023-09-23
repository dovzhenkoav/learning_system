from rest_framework import serializers
from rest_framework.response import Response

from lms.models import Product, Lesson, ViewedLesson


class ViewedLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedLesson
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    view_details = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_view_details(self, instance):
        request = self.context.get("request")
        obj = ViewedLesson.objects.filter(user_id=request.user.id, lesson_id=instance.id)

        if obj:
            obj = obj.first()
            return {
                'max_length': obj.max_length,
                'viewed_length': obj.viewed_length,
                'is_viewed': obj.viewed
            }


class ProductSerializer(serializers.ModelSerializer):
    product_lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_product_lessons(self, instance):
        request = self._context["request"]
        return Lesson.objects.filter(product=instance.id).exists()
