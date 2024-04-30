from django.contrib import admin
from .models import Year, Project,AvailableFont,startPage,Image,PageContent,Gif



class GifAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'Index')  # Отображаемые поля в списке объектов

admin.site.register(Gif, GifAdmin)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']


@admin.register(AvailableFont)
class AvailableFontAdmin(admin.ModelAdmin):
    pass


@admin.register(startPage)
class startPageAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_number', 'page', 'image', 'caption')
    list_filter = ('gallery_number', 'page')
    search_fields = ('page__external_title', 'caption')

# Регистрация модели PageContent в админке
@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_title', 'internal_title', 'title')
    search_fields = ('external_title', 'internal_title', 'title')

    fieldsets = (
        (None, {
            'fields': ('external_title', 'internal_title', 'title', 'text',  'youtube_link', 'video_caption',  'youtube_link2', 'video_caption2', 'youtube_link3', 'video_caption3')
        }),
        ('Дополнительные тестовые переменные', {
            'fields': ('test_variable_1', 'test_variable_2', 'test_variable_3', 'test_variable_4', 'test_variable_5'),
            'classes': ('collapse',),
        }),
        ('Шрифты', {
            'fields': ('font_title', 'font_text', 'font_video_caption', 'font_external_title', 'font_internal_title',
                       'font_test_variable_1', 'font_test_variable_2', 'font_test_variable_3', 'font_test_variable_4', 'font_test_variable_5'),
            'classes': ('collapse',),
        }),
    )


