from django.urls import path
<<<<<<< HEAD
from court import views 
=======
from . import views 
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05
app_name = "court"

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
<<<<<<< HEAD
    path('loginregister/', views.MainView.as_view(), name='login_register'),
=======
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05
    # path('judge/', views.JudgeView.as_view(), name='judge'),
    # path('advocate/', views.AdvocateView.as_view(), name='advocate'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('fileCase/', views.FileCase.as_view(), name='fileCase'),
<<<<<<< HEAD
    path('feecalc/', views.FeesFormView.as_view(), name='feecalc'),
    path('status/<str:cnr>/', views.SearchView.as_view(), name='status'),
    path('search/', views.search, name='search'),
=======
    path('feecalc/', views.feecalc, name='feecalc'),
    path('status/', views.SearchView.as_view(), name='status'),
    # path('search/', views.search, name='search'),
>>>>>>> 80025140d39514c1cc78f16240f96bad1ab73e05
]
