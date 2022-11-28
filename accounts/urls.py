from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path("login/", views.user_login, name="user_login"),
]