from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import AjaxStudent
from django.views.decorators.csrf import csrf_exempt


def student_form_page(request):
    return render(request, 'unique_register.html')

@csrf_exempt
@require_POST
def ajax_register_view(request):
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    email = request.POST.get('email', '').strip()
    if not all([first_name, last_name, email]):
        return JsonResponse({'error': 'All fields are required.'}, status=400)
    if AjaxStudent.objects.filter(email=email).exists():
        return JsonResponse({'error': 'This email is already registered.'}, status=400)
    AjaxStudent.objects.create(first_name=first_name, last_name=last_name,
    email=email)
    return JsonResponse({'message': 'Registration successful!'})