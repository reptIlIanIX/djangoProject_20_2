from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    description = models.TextField(max_length=150, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    description = models.TextField(max_length=150, verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="цена")
    date_start = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    data_end = models.DateTimeField(verbose_name="дата закрытия", **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов

    @property

    def active_version(self):
        return self.version_set.filter(is_active=True).last()


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num = models.IntegerField(verbose_name='номер версии', default=1)
    version_name = models.CharField(max_length=100, verbose_name='версия')
    is_active = models.BooleanField(verbose_name='Активен')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'версии'  # Настройка для наименования набора объектов
