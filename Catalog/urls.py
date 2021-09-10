from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index, name='Index'),
    path('olis/', views.OlisListView.as_view(), name='Olis'),
    path('olis/<typenummer>/', views.OlisProductView.as_view(), name='OlisProduct'),
    path('olis/<Lijn>/<urlsearch>/', views.OlisListView.as_view(), name='Olis'),
    path('search/', views.SearchView, name='Search'),
    
    path('giorik/', views.GiorikListView.as_view(), name='Giorik'),
    path('giorik/<typenummer>', views.GiorikProductView.as_view(), name='GiorikProduct'),
    path('giorik/<Lijn>/<urlsearch>/', views.GiorikListView.as_view(), name='Giorik'),
    ]
