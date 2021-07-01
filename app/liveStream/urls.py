from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/<stream_key>/', views.export, name='export'),
    path('<stream_key>/', views.room, name='room'),
]
