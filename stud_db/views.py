from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Student, Course


# 🏠 Home
def home(request):
    return render(request, 'home.html')


# 👨‍🎓 Student List
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# 📚 Course List
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


# 📝 Register (Enroll Student)
def register(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    if request.method == "POST":
        student_id = request.POST.get('student')
        course_id = request.POST.get('course')

        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)

        student.courses.add(course)

        return render(request, 'success.html', {
            'message': f"{student.name} enrolled in {course.coursename}"
        })

    return render(request, 'register.html', {
        'students': students,
        'courses': courses
    })


# 📊 Enrolled List (Students per Course)
def enrolled_list(request):
    courses = Course.objects.all()
    students = None
    selected_course = None

    if request.method == "POST":
        course_id = request.POST.get('course')
        selected_course = Course.objects.get(id=course_id)
        students = selected_course.students.all()

    return render(request, 'enrolled_list.html', {
        'courses': courses,
        'students': students,
        'selected_course': selected_course
    })
    

# ➕ Add Student
def add_student(request):
    if request.method == "POST":
        usn = request.POST.get('usn')
        name = request.POST.get('name')
        sem = request.POST.get('sem')

        Student.objects.create(
            usn=usn,
            name=name,
            sem=sem
        )

        return redirect('students')

    return render(request, 'add_student.html')


# ➕ Add Course
def add_course(request):
    if request.method == "POST":
        code = request.POST.get('coursecode')
        name = request.POST.get('coursename')
        credits = request.POST.get('credits')

        Course.objects.create(
            coursecode=code,
            coursename=name,
            credits=credits
        )

        return redirect('courses')

    return render(request, 'add_course.html')


# 📋 Generic Class View - Student List
class StudentListView(ListView):
    """Display list of all students using generic ListView"""
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 10  # Optional: paginate results


# 👤 Generic Class View - Student Detail
class StudentDetailView(DetailView):
    """Display details of a specific student with enrolled courses"""
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'