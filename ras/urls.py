
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views

urlpatterns = [

    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index2, name="index2"),
    re_path(r'^app/', include('app.urls')),

]
