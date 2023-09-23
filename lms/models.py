from django.db import models
from django.contrib.auth.models import User

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='продукт')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    students = models.ManyToManyField(User, **NULLABLE)

    def __str__(self):
        return f'Product {self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Lesson(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    video_link = models.URLField(verbose_name='ссылка на урок')
    video_length = models.IntegerField(verbose_name='длительность в секундах')

    # viewed_users = models.ManyToManyField(User)

    def __str__(self):
        return f'Lesson {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class ViewedLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'просмотры уроков'
        verbose_name_plural = 'просмотры уроков'
