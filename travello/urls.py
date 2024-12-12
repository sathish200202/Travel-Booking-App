from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('destination/<int:dest_id>', views.destination, name='destination'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('news', views.news, name="news"),
    path('services', views.services, name="services"),
   


]