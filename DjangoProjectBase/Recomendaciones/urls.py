from django.urls import path
from . import views

urlpatterns = [
    path('', views.Recomendaciones, name='Recomendaciones'),
]