from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('host/', views.host, name='host'),
    path('guest/', views.guest, name='guest'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('profile/', views.profile, name='profile'),

]