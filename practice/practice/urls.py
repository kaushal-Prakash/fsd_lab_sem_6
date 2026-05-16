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
from student import views as student_course
from student_forms import views as student_forms
from generic_class import views as generic_class

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/<int:offset>', offset_views.time),
    path('template_inheritance/about', template_inheritance.about),
    path('template_inheritance/home', template_inheritance.home),
    path('template_inheritance/contact', template_inheritance.contact),
    path('student/student_list',student_course.student_list),
    path('student/enrol_student',student_course.enrol_student),
    path('student_forms/',student_forms.project_view),
    path('generic_class/students',generic_class.StudentListView.as_view(), name='student_list'),
    path('generic_class/students/<int:id>',generic_class.StudentDetailView.as_view(), name='student_detail'),
]
