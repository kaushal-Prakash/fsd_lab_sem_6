from django.shortcuts import render
from .forms import ProjectForm

def project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})
