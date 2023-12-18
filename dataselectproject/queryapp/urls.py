from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'queryapp'

urlpatterns = [
    path('',views.index,
        name='index'),
    path('register/', views.register,
        name='register'),
    path('login/',views.user_login,
        name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='toplantıapp/index.html'),
        name='logout'),
    path('devlet_ekle/', views.devlet_ekle,
        name='devlet_ekle'),
    path('<slug:slug>/', views.details,
        name='details'),
    path('delete/<slug:slug>/', views.delete_devlet,
        name='delete_devlet'),
]