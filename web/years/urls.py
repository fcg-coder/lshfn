from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static


app_name = 'years'

urlpatterns = [
   path('', views.index, name='index'),
   path('polunochnoe/', views.polunochnoe, name='polunochnoe'),
   path('page_view/<int:page_id>/', views.page_view, name='page_view'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)