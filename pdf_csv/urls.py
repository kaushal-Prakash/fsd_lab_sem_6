from django.urls import path
from . import views
urlpatterns = [
    path('reg_ajax/', views.student_form_page, name='student-form-page'),
    path('ajax/register/', views.ajax_register_view, name='ajax-student-register'),
]
