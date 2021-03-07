from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecourt-home'),
    path('about/', views.about, name='ecourt-about'),
]
