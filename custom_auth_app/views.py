from multiprocessing import context
from turtle import title
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Student, Teacher
from .forms import StudentLoginForm, TeacherLoginForm


def welcome_view(request):
    context = {
        'title': 'Welcome to Digi Academy',
    }
    return render(request, 'custom_auth_app/welcome.html', context)


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                messages.success(request, 'Welcome ' + user.username)
                return redirect('sta:student_dashboard',)
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('custom_auth_app:student_login')
    else:
        form = StudentLoginForm()
    return render(request, 'custom_auth_app/student_login.html', {'form': form, 'title': 'Student Login'})


def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_teacher:
                login(request, user)
                messages.success(request, 'Welcome ' + user.username)
                return redirect('sta:teacher_dashboard',)
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('custom_auth_app:teacher_login')
    else:
        form = TeacherLoginForm()
    return render(request, 'custom_auth_app/teacher_login.html', {'form': form, 'title': 'Teacher Login'})


def logout_view(request):
    logout(request)
    return redirect('custom_auth_app:welcome')
