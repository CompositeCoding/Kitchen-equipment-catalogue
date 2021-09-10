from django.urls import path

from . import views


urlpatterns = [
    path('klanten/', views.KlantenView, name='Klanten'),
    ]
