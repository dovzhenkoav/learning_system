from django.urls import path

from lms.views import ProductListView, LessonsListView, lesson_detail, get_streaming_video

app_name = 'lms'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>', LessonsListView.as_view(), name='product-lessons'),
    path('product/lesson/<int:pk>', lesson_detail, name='lesson-details'),
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
]
