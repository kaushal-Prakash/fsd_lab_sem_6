from django.urls import path
from . import views as template_views

urlpatterns = [
    path('', template_views.home, name='home'),
    path('about/', template_views.about, name='about'),
    path('contact/', template_views.contact, name='contact'),
]
