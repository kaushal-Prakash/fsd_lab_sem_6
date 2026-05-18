from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# User Signup View
def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_signin") # Redirect to login page after registration
        else:
            form = UserCreationForm()
            return render(request, "signup_page.html", {"form": form})
        
# User Login View
class UserSigninView(LoginView):
    template_name = "signin_page.html"
    
    def get_success_url(self):
        return reverse_lazy("dashboard")
    
# User Logout View
class UserSignoutView(LogoutView):
    next_page = reverse_lazy("user_signin") # Redirect to login page after logout
    
# Dashboard View (requires login)
@login_required
def dashboard_view(request):
    return render(request, "dashboard.html", {"user": request.user})