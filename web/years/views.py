from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Year, Project,startPage,AvailableFont,PageContent, Image, Gif

import random
# from django_user_agents.utils import get_user_agent


def index(request):
    years = Year.objects.all()
    projects = Project.objects.all()
    font = startPage.objects.filter(id=1).first().font
    content1 = startPage.objects.filter(id=1).first().content1
    content2 = startPage.objects.filter(id=1).first().content2
    gifs = Gif.objects.all()  # Получаем все объекты модели Gif

    pages = PageContent.objects.all()
    return render(request, 'index.html', {'years':years   , 'projects':projects, 'font':font , 'content1':content1,'content2':content2, 'pages':pages , 'gifs': gifs})




def polunochnoe(request):
     # Отобразить страницу для компьютера
    page = PageContent.objects.get(id=10)
    images = Image.objects.filter(page=page)
    gallery_range = set()

    for image in images:
        gallery_range.add(image.gallery_number)

    for image in images:
        image.random_top = random.randint(0, 90)
        image.random_left = random.randint(0, 90)

    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     # Отобразить страницу для мобильного устройства
    #     return render(request, 'page.html', {'page': page, 'images': images, 'gallery_range': gallery_range})
    # elif user_agent.is_tablet:
    #     # Отобразить страницу для планшета
    #     return render(request, 'page.html', {'page': page, 'images': images, 'gallery_range': gallery_range})
    # else:
       

        return render(request, 'polunochnoe1.html', {'page': page, 'images': images, 'gallery_range': gallery_range})


def page_view(request, page_id):


    print(page_id)
    # Получаем объект страницы по её идентификатору
    page = PageContent.objects.get(id=page_id)
    
    print(page)
    
    images = Image.objects.filter(page = page )

    gallery_range = set()

    for image in images:
        gallery_range.add(image.gallery_number)

        print(gallery_range)

    
    print(images)
    # Передаем объект страницы и связанные с ней изображения в шаблон для отображения
    return render(request, 'page.html', {'page': page, 'images': images, 'gallery_range': gallery_range})