# Generated by Django 4.2.7 on 2024-03-24 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('years', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_title', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Внешнее название')),
                ('internal_title', models.CharField(blank=True, max_length=100, verbose_name='Внутреннее название')),
                ('page_id', models.CharField(blank=True, max_length=100, unique=True, verbose_name='ID страницы')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('youtube_link', models.URLField(blank=True, null=True, verbose_name='Ссылка на YouTube видео')),
                ('test_variable_1', models.CharField(blank=True, max_length=100, verbose_name='Тестовая переменная 1')),
                ('test_variable_2', models.CharField(blank=True, max_length=100, verbose_name='Тестовая переменная 2')),
                ('test_variable_3', models.CharField(blank=True, max_length=100, verbose_name='Тестовая переменная 3')),
                ('test_variable_4', models.CharField(blank=True, max_length=100, verbose_name='Тестовая переменная 4')),
                ('test_variable_5', models.CharField(blank=True, max_length=100, verbose_name='Тестовая переменная 5')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_number', models.IntegerField(verbose_name='Номер галереи')),
                ('image', models.ImageField(upload_to='images/')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='Подпись к изображению')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='years.pagecontent')),
            ],
        ),
    ]