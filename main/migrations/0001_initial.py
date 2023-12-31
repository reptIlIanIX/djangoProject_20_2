# Generated by Django 4.2.4 on 2023-08-16 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('description', models.TextField(max_length=150, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('description', models.TextField(max_length=150, verbose_name='описание')),
                ('image', models.ImageField(upload_to='images/', verbose_name='изображение')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('date_start', models.DateTimeField(verbose_name='дата создания')),
                ('data_end', models.DateTimeField(verbose_name='дата закрытия')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
