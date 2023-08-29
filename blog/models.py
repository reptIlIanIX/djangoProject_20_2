from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    topic = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение', **NULLABLE)
    date_start = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(verbose_name='Опубликован')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.topic}, {self.description}'

    class Meta:
        verbose_name = 'блог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'блоги'  # Настройка для наименования набора объектов
