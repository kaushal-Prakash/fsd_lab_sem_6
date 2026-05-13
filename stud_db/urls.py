from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='courses'),
    path('register/', views.register, name='register'),
    path('enrolled/', views.enrolled_list, name='enrolled'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-course/', views.add_course, name='add_course'),
    
    # Generic Class Views
    path('students-list/', views.StudentListView.as_view(), name='student_list_view'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
]