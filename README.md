# Django Laboratory Experiments - Complete Documentation

This repository contains comprehensive Django experiments covering various web development concepts including templating, data models, forms, views, and report generation. Each lab is organized as a separate Django app within the main project.

---

## 📋 Table of Contents

1. [Project Setup](#project-setup)
2. [Lab 1: Date & Time with Server Offset](#lab-1-date--time-with-server-offset)
3. [Lab 2: Template Inheritance & Layout](#lab-2-template-inheritance--layout)
4. [Lab 3: Student Course Enrollment System](#lab-3-student-course-enrollment-system)
5. [Lab 4: Admin Interface & Migrations](#lab-4-admin-interface--migrations)
6. [Lab 5: Model Forms](#lab-5-model-forms)
7. [Lab 6: Generic Class Views (List & Detail)](#lab-6-generic-class-views-list--detail)
8. [Lab 7: CSV & PDF Generation](#lab-7-csv--pdf-generation)
9. [Lab 8: Django Authentication System](#lab-8-django-authentication-system)
10. [Important Django Commands](#important-django-commands)
11. [Project Structure Overview](#project-structure-overview)

---

## 🚀 Project Setup

### Prerequisites
- Python 3.8+
- Django 5.2+
- Required packages (see requirements.txt)

### Initial Setup

```bash
# Navigate to project directory
cd todo_django

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser for admin
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Server will run at: **http://127.0.0.1:8000/**
Admin panel: **http://127.0.0.1:8000/admin/**

---

## 📚 Lab 1: Date & Time with Server Offset

**App Name:** `main`
**Location:** [main/](main/)

### Objective
Develop a Django app that displays:
- Current server date and time
- Date and time four hours ahead (offset +4)
- Date and time four hours behind (offset -4)

### Key Files

| File | Purpose |
|------|---------|
| [main/views.py](main/views.py) | Contains `time()` view that calculates time offsets |
| [main/urls.py](main/urls.py) | URL routing for time view |
| [main/templates/time.html](main/templates/time.html) | Display template for time offset |

### Implementation Steps

1. **Model:** No models required
2. **Views:** Function-based view that calculates time offsets
3. **URL Routing:** Dynamic URL parameter to accept offset values

### View Function

```python
def time(request, offset):
    offset = int(offset)
    curr_time = datetime.datetime.now()
    past = curr_time - datetime.timedelta(hours=offset)
    future = curr_time + datetime.timedelta(hours=offset)
    
    return render(request, "time.html", context={
        "past_time": past,
        "future_time": future,
        "current_time": curr_time,
        "offset": offset,
    })
```

### URL Pattern

```python
path('time/<int:offset>/', views.time, name='time')
```

### How to Access
- **Current Time:** http://127.0.0.1:8000/time/0/
- **4 Hours Ahead:** http://127.0.0.1:8000/time/4/
- **4 Hours Behind:** http://127.0.0.1:8000/time/-4/

### Features Demonstrated
✅ Django views and URL routing
✅ datetime module usage
✅ Template context passing
✅ Dynamic URL parameters

---

## 🎨 Lab 2: Template Inheritance & Layout

**App Name:** `template_inheritance`
**Location:** [template_inheritance/](template_inheritance/)

### Objective
Develop a reusable layout template with:
- Professional header with navigation menu
- Footer with copyright and developer information
- Create 3 pages that inherit from this layout:
  1. Home Page
  2. About Us
  3. Contact Us

### Key Files

| File | Purpose |
|------|---------|
| [template_inheritance/views.py](template_inheritance/views.py) | Views for home, about, contact pages |
| [template_inheritance/urls.py](template_inheritance/urls.py) | URL routing configuration |
| [template_inheritance/templates/layout.html](template_inheritance/templates/layout.html) | Base layout template with header/footer |
| [template_inheritance/templates/home.html](template_inheritance/templates/home.html) | Home page |
| [template_inheritance/templates/about.html](template_inheritance/templates/about.html) | About Us page |
| [template_inheritance/templates/contact.html](template_inheritance/templates/contact.html) | Contact Us page |

### Implementation Steps

1. **Create Base Template (layout.html):**
   - Define HTML structure with navigation menu
   - Add header section with branding
   - Create footer with copyright information
   - Use `{% block content %}` for child pages

2. **Create Child Templates:**
   - Extend base template: `{% extends "layout.html" %}`
   - Override content block with page-specific content

3. **Create Views:** Simple function-based views rendering each page

4. **Configure URLs:** Map URLs to view functions

### Base Template Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>
        <nav><!-- Navigation Menu --></nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2026 My Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

### Child Template Example

```html
{% extends "layout.html" %}

{% block title %}Home - My Website{% endblock %}

{% block content %}
    <h1>Welcome to Our Website</h1>
    <p>This is the home page content...</p>
{% endblock %}
```

### URL Patterns

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

### How to Access
- **Home:** http://127.0.0.1:8000/
- **About Us:** http://127.0.0.1:8000/about/
- **Contact Us:** http://127.0.0.1:8000/contact/

### Features Demonstrated
✅ Django template inheritance
✅ Block system for content reuse
✅ Navigation menus
✅ Static page rendering
✅ DRY principle in templates

---

## 👨‍🎓 Lab 3: Student Course Enrollment System

**App Name:** `stud_db`
**Location:** [stud_db/](stud_db/)

### Objective
Develop a complete student registration system where:
- Students can be registered
- Courses can be created
- Students can enroll in courses
- Display list of students for any selected course
- ManyToMany relationship between Student and Course

### Key Files

| File | Purpose |
|------|---------|
| [stud_db/models.py](stud_db/models.py) | Student and Course models with ManyToMany |
| [stud_db/views.py](stud_db/views.py) | Views for listing, registering, enrollment |
| [stud_db/urls.py](stud_db/urls.py) | URL configuration |
| [stud_db/templates/register.html](stud_db/templates/register.html) | Student enrollment form |
| [stud_db/templates/student_list.html](stud_db/templates/student_list.html) | List all students |
| [stud_db/templates/course_list.html](stud_db/templates/course_list.html) | List all courses |
| [stud_db/templates/enrolled_list.html](stud_db/templates/enrolled_list.html) | Show enrolled students for selected course |

### Models

#### Student Model
```python
class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)  # Unique ID
    name = models.CharField(max_length=100)
    sem = models.IntegerField()  # Semester
    courses = models.ManyToManyField(Course, related_name='students')
```

#### Course Model
```python
class Course(models.Model):
    coursecode = models.CharField(max_length=20, unique=True)
    coursename = models.CharField(max_length=100)
    credits = models.IntegerField()
```

### Implementation Steps

1. **Define Models:**
   - Create Student model with USN, name, semester
   - Create Course model with code, name, credits
   - Add ManyToMany relationship

2. **Create Views:**
   - Home view
   - Student list view
   - Course list view
   - Add student form
   - Add course form
   - Student registration view
   - Enrolled students view

3. **Create Forms:** Use Django HTML forms for data entry

4. **Configure URLs:** Map all views to URL patterns

5. **Create Templates:** Display data with proper HTML structure

### Key Views

```python
def register(request):
    """Enroll a student in a course"""
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

def enrolled_list(request):
    """Show all enrolled students for selected course"""
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
```

### Database Setup

```bash
# Create migrations
python manage.py makemigrations stud_db

# Apply migrations
python manage.py migrate
```

### URL Patterns

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='courses'),
    path('register/', views.register, name='register'),
    path('enrolled/', views.enrolled_list, name='enrolled'),
    path('add-student/', views.add_student, name='add_student'),
    path('add-course/', views.add_course, name='add_course'),
]
```

### How to Access
- **Home:** http://127.0.0.1:8000/stud_db/
- **Students List:** http://127.0.0.1:8000/stud_db/students/
- **Courses List:** http://127.0.0.1:8000/stud_db/courses/
- **Register Student:** http://127.0.0.1:8000/stud_db/register/
- **View Enrolled:** http://127.0.0.1:8000/stud_db/enrolled/
- **Add Student:** http://127.0.0.1:8000/stud_db/add-student/
- **Add Course:** http://127.0.0.1:8000/stud_db/add-course/

### Features Demonstrated
✅ Django Models (Student, Course)
✅ ManyToMany relationships
✅ Django ORM queries
✅ Form handling (POST requests)
✅ Template loops and conditionals
✅ URL routing

---

## 🔧 Lab 4: Admin Interface & Migrations

**App Name:** `stud_db`
**Location:** [stud_db/](stud_db/)

### Objective
Register models in Django admin interface for easy data management through admin forms, and perform database migrations.

### Key Files

| File | Purpose |
|------|---------|
| [stud_db/admin.py](stud_db/admin.py) | Admin interface registration |
| [stud_db/migrations/](stud_db/migrations/) | Database migration files |

### Admin Registration

```python
from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Course)
```

### Implementation Steps

1. **Register Models:** Add models to admin.py
2. **Create Superuser:** Use `createsuperuser` command
3. **Access Admin:** Visit http://127.0.0.1:8000/admin/
4. **Add Data:** Use admin forms to add students and courses
5. **Migrations:** Run makemigrations and migrate commands

### Migration Commands

```bash
# Show migration status
python manage.py showmigrations

# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View SQL of migration
python manage.py sqlmigrate stud_db 0001

# Revert migrations
python manage.py migrate stud_db 0001
```

### Admin Features
✅ CRUD operations for models
✅ Search and filtering
✅ Bulk actions
✅ Data export capabilities
✅ User-friendly interface

### How to Access Admin
1. Create superuser: `python manage.py createsuperuser`
2. Visit: http://127.0.0.1:8000/admin/
3. Login with credentials
4. Manage Student and Course data

---

## 📝 Lab 5: Model Forms

**App Name:** `student_form`
**Location:** [student_form/](student_form/)

### Objective
Develop a Django Model Form for student project information containing:
- Project topic (required)
- Languages used (required)
- Project duration in weeks (required)

### Key Files

| File | Purpose |
|------|---------|
| [student_form/models.py](student_form/models.py) | Project model definition |
| [student_form/forms.py](student_form/forms.py) | ProjectForm ModelForm |
| [student_form/views.py](student_form/views.py) | Form display and submission view |
| [student_form/templates/project_form.html](student_form/templates/project_form.html) | Form display template |
| [student_form/templates/project_success_page.html](student_form/templates/project_success_page.html) | Success confirmation page |

### Model Definition

```python
class Project(models.Model):
    topic = models.CharField(max_length=100)
    languages_used = models.TextField()
    duration = models.PositiveIntegerField()  # in weeks
    
    def __str__(self):
        return self.topic
```

### ModelForm Implementation

```python
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic', 'languages_used', 'duration']
        widgets = {
            'topic': forms.TextInput(attrs={'placeholder': 'Enter project topic'}),
            'languages_used': forms.Textarea(attrs={'placeholder': 'Enter languages used'}),
            'duration': forms.NumberInput(attrs={'placeholder': 'Enter duration in weeks'}),
        }
        labels = {
            'topic': 'Project Topic',
            'languages_used': 'Languages Used for the Project',
            'duration': 'Duration (Weeks)',
        }
```

### View Implementation

```python
from django.shortcuts import render
from .forms import ProjectForm

def project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'project_success_page.html')
    else:
        form = ProjectForm()
    
    return render(request, 'project_form.html', {'form': form})
```

### Implementation Steps

1. **Define Model:** Create Project model with three fields
2. **Create ModelForm:** Inherit from forms.ModelForm
3. **Create View:** Handle GET and POST requests
4. **Create Templates:**
   - Form template with CSRF token
   - Success confirmation page
5. **Configure URLs:** Map view to URL pattern

### How to Access
- **Form:** http://127.0.0.1:8000/student_form/
- **Submit:** Fill form and click submit
- **Success:** Redirect to success page after submission

### Features Demonstrated
✅ Django ModelForm
✅ Custom form widgets
✅ Form validation
✅ CSRF protection
✅ Model instance creation
✅ Form rendering helpers

---

## 📊 Lab 6: Generic Class Views (List & Detail)

**App Name:** `stud_db`
**Location:** [stud_db/](stud_db/)

### Objective
Create generic class views that display:
- ListView: List of all students
- DetailView: Details of a specific student with their enrolled courses

### Key Files

| File | Purpose |
|------|---------|
| [stud_db/views.py](stud_db/views.py) | Contains generic class views (to be updated) |
| [stud_db/urls.py](stud_db/urls.py) | URL routing for class views |
| [stud_db/templates/student_detail.html](stud_db/templates/student_detail.html) | Student details template |

### Implementation

#### Generic ListView

```python
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
```

#### Generic DetailView

```python
from django.views.generic import DetailView
from .models import Student

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'
```

### URL Configuration

```python
from django.urls import path
from . import views

urlpatterns = [
    # ... existing paths ...
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
]
```

### Template Examples

**Student Detail Template:**
```html
{% extends "layout.html" %}

{% block content %}
    <h1>{{ student.name }}</h1>
    <p><strong>USN:</strong> {{ student.usn }}</p>
    <p><strong>Semester:</strong> {{ student.sem }}</p>
    
    <h3>Enrolled Courses</h3>
    <ul>
        {% for course in student.courses.all %}
            <li>{{ course.coursename }} ({{ course.coursecode }})</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### How to Access
- **Student List:** http://127.0.0.1:8000/stud_db/students/
- **Student Detail:** http://127.0.0.1:8000/stud_db/student/1/

### Features Demonstrated
✅ Django Generic Class Views
✅ ListView for list display
✅ DetailView for single object
✅ URL parameters
✅ Context object names
✅ Template rendering
✅ QuerySet handling

---

## 📄 Lab 7: CSV & PDF Generation

**App Name:** `pdf_csv`
**Location:** [pdf_csv/](pdf_csv/)

### Objective
Develop a Django app that generates CSV and PDF reports for course data from the database.

### Key Files

| File | Purpose |
|------|---------|
| [pdf_csv/models.py](pdf_csv/models.py) | Course model |
| [pdf_csv/views.py](pdf_csv/views.py) | Views for CSV and PDF generation |
| [pdf_csv/urls.py](pdf_csv/urls.py) | URL routing |
| [pdf_csv/templates/course_list.html](pdf_csv/templates/course_list.html) | Display courses with download links |

### Model

```python
class Course(models.Model):
    coursecode = models.CharField(max_length=10)
    coursename = models.CharField(max_length=50)
    credits = models.IntegerField()
    
    def __str__(self):
        return f"{self.coursecode} - {self.coursename}"
```

### CSV Generation

```python
import csv
from django.http import HttpResponse
from .models import Course

def generateCSV(request):
    """Generate CSV file of all courses"""
    courses = Course.objects.all()
    resp = HttpResponse(content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename=course_data.csv'
    
    writer = csv.writer(resp)
    writer.writerow(['Course Code', 'Course Name', 'Course Credits'])
    
    for c in courses:
        writer.writerow([c.coursecode, c.coursename, c.credits])
    
    return resp
```

### PDF Generation

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from .models import Course

def generatePDF(request):
    """Generate PDF file of all courses"""
    courses = Course.objects.all()
    resp = HttpResponse(content_type="application/pdf")
    resp['Content-Disposition'] = 'attachment; filename=course_data.pdf'
    
    # Create PDF document
    pdf = SimpleDocTemplate(resp, pagesize=A4)
    
    # Prepare table data
    table_data = [['Course Code', 'Course Name', 'Course Credits']]
    
    for c in courses:
        table_data.append([c.coursecode, c.coursename, str(c.credits)])
    
    # Create table with styling
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    # Build and return PDF
    pdf.build([table])
    return resp
```

### URL Configuration

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('export-csv/', views.generateCSV, name='export_csv'),
    path('export-pdf/', views.generatePDF, name='export_pdf'),
]
```

### How to Access
- **View Courses:** http://127.0.0.1:8000/pdf_csv/
- **Download CSV:** http://127.0.0.1:8000/pdf_csv/export-csv/
- **Download PDF:** http://127.0.0.1:8000/pdf_csv/export-pdf/

### Features Demonstrated
✅ CSV file generation and download
✅ PDF file generation using reportlab
✅ HttpResponse with file attachment
✅ Dynamic data from database
✅ Table formatting in PDF
✅ File download handling

### Required Package

```bash
pip install reportlab
```

---

## � Lab 8: Django Authentication System

**App Name:** `login_signup`
**Location:** [practice/login_signup/](practice/login_signup/)

### Objective
Develop a Django application that allows users to:
- Register with a new account using UserCreationForm
- Log in with username and password
- Log out and be redirected to the login page
- View a protected dashboard only when authenticated
- Use Django's built-in authentication system

### Key Features
✅ User registration with password validation
✅ User login with Django's LoginView
✅ User logout with Django's LogoutView
✅ Login-required decorator for protected views
✅ User authentication and session management
✅ Form validation and error handling

### Key Files

| File | Purpose |
|------|---------|
| [practice/login_signup/views.py](practice/login_signup/views.py) | Views for signup, signin, signout, and dashboard |
| [practice/login_signup/urls.py](practice/login_signup/urls.py) | URL routing with named patterns |
| [practice/login_signup/templates/signup_page.html](practice/login_signup/templates/signup_page.html) | User registration form |
| [practice/login_signup/templates/signin_page.html](practice/login_signup/templates/signin_page.html) | User login form |
| [practice/login_signup/templates/dashboard.html](practice/login_signup/templates/dashboard.html) | Protected user dashboard |

### Models

No custom models are required. Uses Django's built-in `User` model from `django.contrib.auth.models`.

### Views Implementation

#### User Signup View
```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def user_signup(request):
    """Handle user registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_signin")  # Redirect to login after signup
    else:
        form = UserCreationForm()
    
    return render(request, "signup_page.html", {"form": form})
```

#### User Login View
```python
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserSigninView(LoginView):
    """Handle user login using Django's built-in LoginView"""
    template_name = "signin_page.html"
    
    def get_success_url(self):
        """Redirect to dashboard after successful login"""
        return reverse_lazy("dashboard")
```

#### User Logout View
```python
from django.contrib.auth.views import LogoutView

class UserSignoutView(LogoutView):
    """Handle user logout using Django's built-in LogoutView"""
    next_page = reverse_lazy("user_signin")  # Redirect to login after logout
```

#### Protected Dashboard View
```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    """Display dashboard - only for authenticated users"""
    return render(request, "dashboard.html", {"user": request.user})
```

### URL Configuration

```python
from django.urls import path
from login_signup import views as login_signup

urlpatterns = [
    path('login_signup/signup', login_signup.user_signup, name='user_signup'),
    path('login_signup/signin', login_signup.UserSigninView.as_view(), name='user_signin'),
    path('login_signup/signout', login_signup.UserSignoutView.as_view(), name='user_signout'),
    path('login_signup/dashboard', login_signup.dashboard_view, name='dashboard'),
]
```

### Templates

#### signup_page.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <p>Already have an account? <a href="{% url 'user_signin' %}">Login here</a></p>
</body>
</html>
```

#### signin_page.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>User Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="{% url 'user_signup' %}">Sign up here</a></p>
</body>
</html>
```

#### dashboard.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h2>Welcome, {{ user.username }}!</h2>
    {% if user.is_authenticated %}
        <p>You are logged in. Feel free to explore!</p>
        <form action="{% url 'user_signout' %}" method="post">
            {% csrf_token %}
            <button type="submit">Sign Out</button>
        </form>
    {% else %}
        <p><a href="{% url 'user_signin' %}">Please login first</a></p>
    {% endif %}
</body>
</html>
```

### Django Settings Configuration

Ensure these settings are in `settings.py`:

```python
# Authentication settings
LOGIN_URL = 'user_signin'  # URL name for login redirect
LOGIN_REDIRECT_URL = 'dashboard'  # URL name after successful login
LOGOUT_REDIRECT_URL = 'user_signin'  # URL name after logout

# Add authentication app if not already included
INSTALLED_APPS = [
    'django.contrib.auth',  # Must be included for User model
    'django.contrib.contenttypes',
    # ... other apps ...
    'login_signup',
]
```

### How to Access

- **Sign Up:** http://127.0.0.1:8000/login_signup/signup
- **Sign In:** http://127.0.0.1:8000/login_signup/signin
- **Dashboard:** http://127.0.0.1:8000/login_signup/dashboard (requires login)
- **Sign Out:** Click "Sign Out" button on dashboard

### Features Demonstrated
✅ Django's built-in User model
✅ UserCreationForm for registration
✅ Class-based views (LoginView, LogoutView)
✅ Function-based views with decorators
✅ Authentication decorators (@login_required)
✅ User sessions management
✅ Redirect URL patterns using reverse_lazy
✅ CSRF token protection
✅ User object and authentication context

### Implementation Steps

1. **Create App:**
   ```bash
   python manage.py startapp login_signup
   ```

2. **Create Templates:** Create signup_page.html, signin_page.html, and dashboard.html

3. **Create Views:** Implement signup, signin, signout, and dashboard views

4. **Configure URLs:** Map all views with named URL patterns

5. **Update Settings:** Add login redirects and configure authentication

6. **Test:** Register a user, login, view dashboard, and logout

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Reverse for 'user_signout' not found" | Ensure all URL patterns have `name` attributes |
| 404 on login_signup pages | Check that app is in INSTALLED_APPS and URLs are registered |
| Redirects not working | Verify LOGIN_URL and LOGIN_REDIRECT_URL in settings.py |
| CSRF token missing error | Add `{% csrf_token %}` in form templates |

---

## �📌 Important Django Commands

### Project Management

```bash
# Create new project
django-admin startproject project_name

# Create new app
python manage.py startapp app_name

# Run development server
python manage.py runserver
python manage.py runserver 8080  # Custom port

# Create superuser
python manage.py createsuperuser

# Database shell
python manage.py shell
```

### Migrations

```bash
# Show all migrations
python manage.py showmigrations

# Create migrations for changes
python manage.py makemigrations

# Create empty migration
python manage.py makemigrations app_name --empty app_name --name migration_name

# Apply migrations
python manage.py migrate

# Show migration details
python manage.py sqlmigrate app_name migration_number

# Revert to specific migration
python manage.py migrate app_name migration_number
```

### Utilities

```bash
# Run tests
python manage.py test

# Check for issues
python manage.py check

# Collect static files
python manage.py collectstatic

# Flush database
python manage.py flush

# Load fixtures
python manage.py loaddata fixture_name
```

---

## 📁 Project Structure Overview

```
todo_django/
├── manage.py                          # Django management script
├── db.sqlite3                         # SQLite database
├── requirements.txt                   # Project dependencies
├── README.md                          # This file
│
├── todo/                              # Main project settings
│   ├── settings.py                    # Project settings
│   ├── urls.py                        # Main URL routing
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│
├── main/                              # Lab 1 - Date & Time
│   ├── models.py
│   ├── views.py                       # time() view with offset
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── tasks.html
│   │   ├── time.html                  # Time display with offset
│   │   └── age_calculator.html
│   └── migrations/
│
├── template_inheritance/              # Lab 2 - Template Inheritance
│   ├── models.py
│   ├── views.py                       # home, about, contact views
│   ├── urls.py
│   ├── admin.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── layout.html                # Base template
│   │   ├── home.html                  # Home page
│   │   ├── about.html                 # About Us page
│   │   └── contact.html               # Contact Us page
│   └── migrations/
│
├── stud_db/                           # Lab 3, 4, 6 - Student System
│   ├── models.py                      # Student & Course models
│   ├── views.py                       # Views for enrollment
│   ├── urls.py
│   ├── admin.py                       # Admin registration
│   ├── forms.py                       # Forms for student/course
│   ├── templates/
│   │   ├── home.html
│   │   ├── student_list.html
│   │   ├── course_list.html
│   │   ├── register.html
│   │   ├── enrolled_list.html
│   │   ├── add_student.html
│   │   ├── add_course.html
│   │   ├── success.html
│   │   └── student_detail.html        # For DetailView
│   └── migrations/
│       ├── 0001_initial.py            # Initial migration
│
├── student_form/                      # Lab 5 - Model Forms
│   ├── models.py                      # Project model
│   ├── views.py                       # Form view
│   ├── urls.py
│   ├── forms.py                       # ProjectForm
│   ├── admin.py
│   ├── templates/
│   │   ├── project_form.html          # Form template
│   │   ├── project_success_page.html  # Success page
│   │   └── student_details_page.html
│   └── migrations/
│
├── pdf_csv/                           # Lab 7 - CSV & PDF Generation
│   ├── models.py                      # Course model
│   ├── views.py                       # CSV & PDF generation views
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── course_list.html           # Display with download links
│   └── migrations/
│
├── practice/                          # Practice project (contains Lab 8 and others)
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── practice/                      # Project settings
│   │   ├── settings.py
│   │   ├── urls.py                    # Main URL routing for practice
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── login_signup/                  # Lab 8 - Authentication System
│   │   ├── models.py
│   │   ├── views.py                   # Signup, signin, signout, dashboard views
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── templates/
│   │   │   ├── signup_page.html       # User registration form
│   │   │   ├── signin_page.html       # User login form
│   │   │   ├── dashboard.html         # Protected user dashboard
│   │   │   └── Unique_register.html
│   │   └── migrations/
│   │
│   └── ... (other practice apps)
│
└── ... (other apps)
```

---

## 🎯 Learning Outcomes

After completing these laboratories, you will understand:

1. **Django Views & URLs**
   - Function-based views
   - Generic class-based views
   - URL routing and parameters

2. **Django Models**
   - Model creation and relationships
   - ManyToMany relationships
   - Model managers and queries

3. **Django Forms**
   - ModelForms
   - Form validation
   - Widget customization

4. **Django Templates**
   - Template inheritance
   - Template tags and filters
   - Context passing

5. **Django Admin**
   - Model registration
   - Admin interface customization
   - Data management

6. **Database Migrations**
   - Creating migrations
   - Applying migrations
   - Migration dependencies

7. **File Generation**
   - CSV export
   - PDF generation
   - File downloads

8. **Web Development Concepts**
   - HTTP methods (GET, POST)
   - CSRF protection
   - RESTful principles

---

## 💡 Tips for Development

1. **Always activate virtual environment** before working
2. **Run migrations** after model changes: `python manage.py migrate`
3. **Use Django shell** for testing queries: `python manage.py shell`
4. **Check for errors**: `python manage.py check`
5. **Use `.gitignore`** to exclude venv, *.pyc, db.sqlite3
6. **Follow naming conventions**: models are singular, apps are plural
7. **Use QuerySet methods** for database queries (filter, exclude, get)
8. **Write docstrings** for views and models

---

## 📚 Additional Resources

- **Django Official Docs:** https://docs.djangoproject.com/
- **Django Templates:** https://docs.djangoproject.com/en/stable/topics/templates/
- **Django Models:** https://docs.djangoproject.com/en/stable/topics/db/models/
- **Django Forms:** https://docs.djangoproject.com/en/stable/topics/forms/
- **ReportLab Documentation:** https://www.reportlab.com/docs/reportlab-userguide.pdf

---

## ✅ Checklist for Completion

- [ ] Lab 1: Date & Time functionality working correctly
- [ ] Lab 2: Template inheritance with all 3 pages
- [ ] Lab 3: Student enrollment system operational
- [ ] Lab 4: Admin interface populated with test data
- [ ] Lab 5: Model form accepting project data
- [ ] Lab 6: Generic views showing list and details
- [ ] Lab 7: CSV and PDF generation working

---

## 👨‍💻 Developer Information

**Created:** 2026
**Technology Stack:** Django 5.2, Python 3.8+, SQLite
**Purpose:** Educational - Learning Django web framework fundamentals

---

## 📝 Notes

- Always backup the database before major changes
- Test functionality in development before deploying
- Use Django's built-in security features (CSRF, XSS protection)
- Keep sensitive information in environment variables
- Follow PEP 8 style guide for Python code

---

**Happy Learning! 🎓**