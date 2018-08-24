from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactezmoi/', views.contactezmoi, name='contactezmoi'),
    path('abayatgallery/', views.abayatgallery, name='abayatgallery'),
    path('burkinigallery/', views.burkinigallery, name='burkinigallery'),
    path('scarfgallery/', views.scarfgallery, name='scarfgallery'),
    path('eidgallery/', views.eidgallery, name='eidgallery'),
    path('defiledemode/', views.defiledemode, name='defiledemode'),
    path('summergallery/', views.summergallery, name='summergallery'), ]
