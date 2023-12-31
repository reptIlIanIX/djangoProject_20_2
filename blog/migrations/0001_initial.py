# Generated by Django 4.2.4 on 2023-08-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='изображение')),
                ('date_start', models.DateTimeField(blank=True, null=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(verbose_name='Опубликован')),
                ('views_count', models.IntegerField(verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
