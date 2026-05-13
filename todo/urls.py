from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),   # Lab 1: Date & Time with offset
    path("pages/", include("template_inheritance.urls")),   # Lab 2: Template Inheritance
    path("stud_db/", include("stud_db.urls")),   # Lab 3, 4, 6: Student Enrollment System
    path("library/", include("library.urls")),   # Library management app
    path("student/", include("student_form.urls")),   # Lab 5: Student Forms
    path("ajax/", include("ajax.urls")),   # AJAX app
    path("pdf_csv/", include("pdf_csv.urls"))   # Lab 7: CSV & PDF Generation
]
