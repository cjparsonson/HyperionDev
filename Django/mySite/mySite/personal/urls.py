from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('coding/', views.coding, name='coding')
]