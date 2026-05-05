from django.urls import path
from .views import course_list, generateCSV, generatePDF

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('courses/generateCSV/', generateCSV, name='generate_csv'),
    path('courses/generatePDF/', generatePDF, name='generate_pdf'),
]
