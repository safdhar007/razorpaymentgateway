
from django.urls import re_path
from . import views
from django.urls import path, re_path

urlpatterns = [
	path('', views.homepage, name='index'),


]
