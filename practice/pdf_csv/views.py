from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from student.models import Course

def generateCSV(request):
    courses = Course.objects.all()
    res = HttpResponse(content_type='text/csv')
    res['Content-Disposition'] = 'attachment; filename=data.csv'
    
    writer = csv.writer(res)
    
    writer.writerow(['Course Name','Credits'])
    for course in courses:
        writer.writerow([course.name,course.credits])
        
    return res

def generatePDF(request):
    courses = Course.objects.all()
    res = HttpResponse(content_type="application/pdf")
    res['Content-Disposition'] = 'attachment; filename=data.pdf'
    
    pdf = SimpleDocTemplate(res, pagesize=A4)
    
    table_data = [['Course Name', 'Credits']]
    
    for c in courses:
        table_data.append([c.name, str(c.credits)])
    
    table = Table(table_data)
    
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    # ('GRID', start, end, thickness, color)
    # (-1,-1) -> means ending cell
    ('BACKGROUND', (0,0), (-1,0), colors.grey)
    # ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke)
    # ('ALIGN', (0,0), (-1,-1), 'CENTER')
    # ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    # ('FONTSIZE', (0,0), (-1,-1), 12)
    # ('BOTTOMPADDING', (0,0), (-1,0), 12)
    # ('BACKGROUND', (0,1), (-1,-1), colors.beige)
    # ('GRID', (0,0), (-1,-1), 1, colors.black)
    print(TableStyle.__doc__)
    pdf.build([table])
    return res
