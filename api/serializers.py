from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User

from lms.models import Product, Lesson, ViewedLesson


class ViewedLessonSerializer(serializers.ModelSerializer):
    """Serializer for ViewedLesson model."""
    class Meta:
        model = ViewedLesson
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Get lesson data with view details on it."""
    view_details = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_view_details(self, instance) -> dict:
        request = self.context.get("request")
        obj = ViewedLesson.objects.filter(user_id=request.user.id, lesson_id=instance.id)

        if obj:
            obj = obj.first()
            return {
                'max_length': obj.max_length,
                'viewed_length': obj.viewed_length,
                'is_viewed': obj.viewed,
                'viewed_date': obj.viewed_date,
            }


class ProductSerializer(serializers.ModelSerializer):
    """Get product data with lessons details on it."""
    product_lessons = LessonSerializer(source='lesson', many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_product_lessons(self, instance):
        request = self._context["request"]
        return Lesson.objects.filter(product=instance.id).exists()


class StatisticsSerializer(serializers.ModelSerializer):
    """Serializer only for statistics view."""
    views_from_students = serializers.SerializerMethodField()
    total_viewed_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_views_from_students(self, instance) -> int:
        """Get all counted view by all students for lesson."""
        lessons = Lesson.objects.filter(product=instance)
        counter = 0
        for lesson in lessons:
            queryset = ViewedLesson.objects.filter(lesson_id=lesson.id)
            if queryset:
                for entry in queryset:
                    if entry.viewed:
                        counter += 1
        return counter

    def get_total_viewed_time(self, instance) -> int:
        """Get all view time in bits by all students for lesson."""
        lessons = Lesson.objects.filter(product=instance)
        counter = 0
        for lesson in lessons:
            queryset = ViewedLesson.objects.filter(lesson_id=lesson.id)
            if queryset:
                for entry in queryset:
                    if entry.viewed_length:
                        counter += entry.viewed_length  # in bits
        return counter

    def get_total_students(self, instance) -> int:
        """Get all students on product."""
        self.course_students_count = len(instance.students.select_related())
        return self.course_students_count

    def get_purchase_percentage(self, instance) -> str:
        """Get percentage from users who purchased course to all users."""
        all_users_count = len(User.objects.all())
        return f'{self.course_students_count / all_users_count * 100:.2f}%'
