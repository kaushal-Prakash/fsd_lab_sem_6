from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
import csv
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def course_list(request):
    """Display the list of courses"""
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'course_list1': courses})


def generateCSV(request):
    """Generate CSV file of all courses"""
    courses = Course.objects.all()
    resp = HttpResponse(content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename=course_data.csv'
    
    # Create a CSV writer object
    writer = csv.writer(resp)
    writer.writerow(['Course Code', 'Course Name', 'Course Credits'])  # Header row
    
    # Write each course's data row
    for c in courses:
        writer.writerow([c.coursecode, c.coursename, c.credits])
    
    return resp


def generatePDF(request):
    """Generate PDF file of all courses"""
    courses = Course.objects.all()
    resp = HttpResponse(content_type="application/pdf")
    resp['Content-Disposition'] = 'attachment; filename=course_data.pdf'
    
    # Create the PDF document
    pdf = SimpleDocTemplate(resp, pagesize=A4)
    
    # Prepare table data
    table_data = [['Course Code', 'Course Name', 'Course Credits']]  # Header row
    
    # Add rows for each course
    for c in courses:
        table_data.append([c.coursecode, c.coursename, str(c.credits)])
    
    # Create the table with styling
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    # Build and return PDF
    pdf.build([table])
    return resp
