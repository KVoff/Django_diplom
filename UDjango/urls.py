"""
URL configuration for UDjango project.

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
from django.urls import path, include
from django.views.generic import TemplateView

from products.views import product_list, product_detail, product_update, \
    product_delete, product_create

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='main.html')),
    path('buyers/', include('buyers.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    # path('profiles/', include('profiles.urls')),
]
