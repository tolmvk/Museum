"""
URL configuration for projectX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from appX import views

urlpatterns = [
    re_path ('contact/', TemplateView.as_view(template_name="XXX/contact.html")),
    re_path ('about/' , TemplateView.as_view(template_name="XXX/about.html")),
    path('details/', views.details),
    path('', views.index,),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
    path('admin/', admin.site.urls),
]
