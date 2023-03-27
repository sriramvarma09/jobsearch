from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Home),
    path('Jobs/about.html',views.About),
    path('Jobs/login.html',views.login),
]