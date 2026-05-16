from django.views.generic import ListView, DetailView
from student.models import Student

# context_object_name in Django is the variable name used inside the HTML template to access data sent from the view.

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'id'
    