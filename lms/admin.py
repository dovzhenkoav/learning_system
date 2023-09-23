from django.contrib import admin

from lms.models import Product, Lesson, ViewedLesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_filter = ('owner',)
    search_fields = ('title', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ViewedLesson)
class ViewedLessonAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'user']

