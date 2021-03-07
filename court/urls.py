from django.urls import path
from . import views 
app_name = "court"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]
