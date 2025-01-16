from django.urls import path
from . import views
from .views import splash

urlpatterns = [
    path('', views.splash, name='splash'),
    path('home', views.home, name='home'),
    path('index1.html', views.index1, name='index1'),
    path('index2.html', views.index1, name='index2'),
    path('register.html',views.register, name='register'),
    path('login.html',views.login, name='login'),

]
