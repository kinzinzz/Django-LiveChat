from django.urls import re_path, path
from django.conf.urls import include
from django.contrib import admin
from accounts import views

urlpatterns = [
    re_path(r'^chat/', include('chat.urls')),
    re_path(r'^admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.index)
]