from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    description = models.TextField(max_length=150, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    description = models.TextField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="цена")
    date_start = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="дата закрытия", **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов



