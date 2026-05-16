from django.shortcuts import render
from .models import Student, Course

# Create your views here.
def student_list(request):
    courses = Course.objects.all()
    students = None
    
    if request.method == "POST":
        course_id = request.POST.get("course")
        students = courses.get(id=course_id).students.all()
    
    return render(request,"student_list.html", context={
        "courses" : courses,
        "students" : students
    })

def enrol_student(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    
    if request.method == "POST":
        student_id = request.POST.get("student")
        course_id = request.POST.get("course")
        
        course = courses.get(id=course_id)
        student = students.get(id=student_id)
        
        student.courses.add(course)
        
        return render(request, 'success.html', {
            'message': f"{student.name} enrolled in {course.name} successfully!!"
        })
        
    return render(request,'enrol_student.html',context={
        'courses': courses,
        'students': students
    })
    