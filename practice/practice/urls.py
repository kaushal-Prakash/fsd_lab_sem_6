"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from time_offset import views as offset_views
from template_inheritance import views as template_inheritance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/<int:offset>', offset_views.time),
    path('template_inheritance/about', template_inheritance.about),
    path('template_inheritance/home', template_inheritance.home),
    path('template_inheritance/contact', template_inheritance.contact),
]
