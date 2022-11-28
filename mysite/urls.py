from django.urls import re_path
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    re_path(r'^chat/', include('chat.urls')),
    re_path(r'^admin/', admin.site.urls),
]