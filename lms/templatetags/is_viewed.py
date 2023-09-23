from django import template
from django.conf import settings

from lms.models import ViewedLesson

register = template.Library()


@register.simple_tag
def viewed(user_id: int, lesson_id: int):
    if not ViewedLesson.objects.filter(lesson_id=lesson_id, user_id=user_id).exists():
        viewed_lesson = ViewedLesson.create(lesson_id=lesson_id, user_id=user_id)
    else:
        viewed_lesson = ViewedLesson.objects.get(lesson_id=lesson_id, user_id=user_id)

    if not viewed_lesson.viewed:
        all_view = viewed_lesson.max_length
        current_view = viewed_lesson.viewed_length
        if (current_view * 100 / all_view) > 80:
            viewed_lesson.viewed = True
            viewed_lesson.save()
            return True
        return False
    return True

@register.simple_tag
def length(video_length: int):
    mins = video_length // 60
    secs = video_length % 60
    hours = mins // 60
    mins = mins % 60
    return f'{hours}:{mins}:{secs}'
