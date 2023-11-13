from django.contrib import admin
from django.urls import path
from . import views
app_name = 'planejamento'
urlpatterns = [
    path('', views.homepage, name = 'homepage' ),
     path('detalhe/<slug:slug>/', views.obra, name = 'obra'),
]
