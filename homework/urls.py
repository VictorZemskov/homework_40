"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webapp.views import index_view, products_view, product_view, about_view, contacts_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='product__index'),
    path('create', products_view, name='product__create'),
    path('product/<int:product_pk>', product_view, name='product__view'),
    path('about', about_view, name='product__about'),
    path('contacts', contacts_view, name='product__contacts')
]

