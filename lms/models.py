from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lesson')

    video_link = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
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
    max_length = models.BigIntegerField(**NULLABLE)
    viewed_length = models.BigIntegerField(**NULLABLE)
    viewed = models.BooleanField(verbose_name='просмотрено', default=False)

    viewed_date = models.DateTimeField(auto_now=True, verbose_name='дата просмотра')

    def __str__(self):
        return f'{self.lesson} {self.user} {self.max_length} {self.viewed_length}'

    class Meta:
        verbose_name = 'просмотры уроков'
        verbose_name_plural = 'просмотры уроков'
