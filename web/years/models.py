from django.db import models

class AvailableFont(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.year)

class Project(models.Model):
    name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True)





    
    def __str__(self):
        return self.name



class Gif(models.Model):
    image = models.ImageField(upload_to='images/')  # Поле для загрузки картинки
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка')
   
    Index = models.ForeignKey('startPage', related_name='images', on_delete=models.CASCADE, default=1)
class startPage(models.Model):
    content1 = models.CharField(max_length=100000000000)
    content2 = models.CharField(max_length=100000000000)
    name = models.CharField(max_length=200)
    font = models.ForeignKey(AvailableFont, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.name)

class Image(models.Model):
    gallery_number = models.IntegerField(verbose_name='Номер галереи')
    page = models.ForeignKey('PageContent', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')  # Поле для загрузки картинки
    caption = models.CharField(max_length=255, verbose_name='Подпись к изображению', blank=True)
class PageContent(models.Model):
    project = models.ForeignKey(Project, related_name='pages', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Проект')
    external_title = models.CharField(max_length=100000000, unique=True, verbose_name='Внешнее название', blank=True)
    internal_title = models.CharField(max_length=100000000, verbose_name='Внутреннее название', blank=True)
    title = models.CharField(max_length=100000000, verbose_name='Заголовок', blank=True)
    text = models.TextField(verbose_name='Текст', blank=True)
    youtube_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на YouTube видео')
    video_caption = models.CharField(max_length=255, verbose_name='Подпись к видео', blank=True)
    count_of_galery = models.IntegerField(verbose_name='Количество галерей', default=1, blank=True)
    
    # Шрифты для основных текстовых переменных
    font_title = models.ForeignKey(AvailableFont, related_name='font_title', on_delete=models.CASCADE, default=1, verbose_name='Шрифт заголовка') 
    font_text = models.ForeignKey(AvailableFont, related_name='font_text', on_delete=models.CASCADE, default=1, verbose_name='Шрифт текста') 
    font_video_caption = models.ForeignKey(AvailableFont, related_name='font_video_caption', on_delete=models.CASCADE, default=1, verbose_name='Шрифт подписи к видео') 
    font_external_title = models.ForeignKey(AvailableFont, related_name='font_external_title', on_delete=models.CASCADE, default=1, verbose_name='Шрифт внешнего названия') 
    font_internal_title = models.ForeignKey(AvailableFont, related_name='font_internal_title', on_delete=models.CASCADE, default=1, verbose_name='Шрифт внутреннего названия') 

    # Дополнительные текстовые переменные
    test_variable_1 = models.CharField(max_length=100000000, blank=True, verbose_name='Тестовая переменная 1')
    test_variable_2 = models.CharField(max_length=100000000, blank=True, verbose_name='Тестовая переменная 2')
    test_variable_3 = models.CharField(max_length=100000000, blank=True, verbose_name='Тестовая переменная 3')
    test_variable_4 = models.CharField(max_length=100000000, blank=True, verbose_name='Тестовая переменная 4')
    test_variable_5 = models.CharField(max_length=100000000, blank=True, verbose_name='Тестовая переменная 5')

    # Шрифты для дополнительных текстовых переменных
    font_test_variable_1 = models.ForeignKey(AvailableFont, related_name='font_test_variable_1', on_delete=models.CASCADE, default=1, verbose_name='Шрифт тестовой переменной 1') 
    font_test_variable_2 = models.ForeignKey(AvailableFont, related_name='font_test_variable_2', on_delete=models.CASCADE, default=1, verbose_name='Шрифт тестовой переменной 2') 
    font_test_variable_3 = models.ForeignKey(AvailableFont, related_name='font_test_variable_3', on_delete=models.CASCADE, default=1, verbose_name='Шрифт тестовой переменной 3') 
    font_test_variable_4 = models.ForeignKey(AvailableFont, related_name='font_test_variable_4', on_delete=models.CASCADE, default=1, verbose_name='Шрифт тестовой переменной 4') 
    font_test_variable_5 = models.ForeignKey(AvailableFont, related_name='font_test_variable_5', on_delete=models.CASCADE, default=1, verbose_name='Шрифт тестовой переменной 5') 

    youtube_link2 = models.URLField(blank=True, null=True, verbose_name='Ссылка на YouTube видео 2')
    youtube_link3 = models.URLField(blank=True, null=True, verbose_name='Ссылка на YouTube видео 3')
   
    video_caption2 = models.CharField(max_length=255, verbose_name='Подпись к видео 2', blank=True)
    video_caption3 = models.CharField(max_length=255, verbose_name='Подпись к видео 3', blank=True)


    def __str__(self):
        return self.title if self.title else 'Страница без названия'
