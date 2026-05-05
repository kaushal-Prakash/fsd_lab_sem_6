from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("main.urls")),   # maps main app url from this urls file
    # path("", include("template_inheritance.urls")),   # maps template_inheritance app url from this urls file
    # path("", include("stud_db.urls")),   # maps stud_db app url from this urls file
    # path("library/", include("library.urls")),
    # path("student/", include("student_form.urls")),
    path("", include("ajax.urls"))
]
