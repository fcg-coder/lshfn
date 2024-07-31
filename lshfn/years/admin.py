from django.contrib import admin
from .models import Year, Project, AvailableFont, startPage, Image, PageContent, Gif

class GifAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'link', 'Index')
    list_display_links = ('id', 'image')
    search_fields = ('image', 'link')
    list_filter = ('Index',)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year']
    search_fields = ['year']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'link']
    search_fields = ['name', 'year__year', 'link']
    list_filter = ['year']

@admin.register(AvailableFont)
class AvailableFontAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(startPage)
class startPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'content1', 'content2', 'font', 'pdf_file']
    search_fields = ['name', 'content1', 'content2', 'font__name']
    list_filter = ['font']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery_number', 'page', 'image', 'caption')
    list_display_links = ('id', 'image')
    search_fields = ('page__external_title', 'caption')
    list_filter = ('gallery_number', 'page')

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'external_title', 'internal_title', 'title')
    search_fields = ('external_title', 'internal_title', 'title', 'project__name')
    list_filter = ('project',)
    fieldsets = (
        ('Основные данные', {
            'fields': ('project', 'external_title', 'internal_title', 'title', 'text', 'youtube_link', 'video_caption', 'count_of_galery')
        }),
        ('Шрифты', {
            'fields': ('font_title', 'font_text', 'font_video_caption', 'font_external_title', 'font_internal_title',
                       'font_test_variable_1', 'font_test_variable_2', 'font_test_variable_3', 'font_test_variable_4', 'font_test_variable_5'),
            'classes': ('collapse',),
        }),
        ('Дополнительные данные', {
            'fields': ('test_variable_1', 'test_variable_2', 'test_variable_3', 'test_variable_4', 'test_variable_5',
                       'youtube_link2', 'video_caption2', 'youtube_link3', 'video_caption3'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Gif, GifAdmin)
