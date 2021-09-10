from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegisterView, name='Register'),
    path('login/', views.Login.as_view(), name='Login'),
    path('logout/', views.Logout.as_view(), name='Logout'),
    path('contact/', views.ContactView, name='Contact'),
    ]
