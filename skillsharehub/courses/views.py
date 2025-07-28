from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import ListView
from .forms import RegisterForm, LoginForm
from .models import Course

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = RegisterForm()
    return render(request, 'courses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('course_list')
    form = LoginForm()
    return render(request, 'courses/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
