from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from cadmin.models import Visitor
from .forms import StudentLoginForm, TeacherLoginForm


def visitor_ip_address(request):
    return x_forwarded_for.split(',')[0] if (
        x_forwarded_for := request.META.get('HTTP_X_FORWARDED_FOR')) else request.META.get('REMOTE_ADDR')


def welcome_view(request):
    ip = visitor_ip_address(request)
    if Visitor.objects.filter(ip_address__iexact=ip).exists():
        v = Visitor.objects.filter(ip_address__iexact=ip).first()
        v.count = v.count + 1
        v.save()
    else:
        Visitor.objects.create(
            ip_address=ip,
            count=1
        )
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
                messages.success(request, f'Welcome {user.username}')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('sta:student_dashboard', )
            else:
                messages.error(request, 'Invalid username or password')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
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
                messages.success(request, f'Welcome {user.username}')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('sta:teacher_dashboard', )
            else:
                messages.error(request, 'Invalid username or password')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('custom_auth_app:teacher_login')
    else:
        form = TeacherLoginForm()
    return render(request, 'custom_auth_app/teacher_login.html', {'form': form, 'title': 'Teacher Login'})


def student_logout_view(request):
    logout(request)
    return redirect('custom_auth_app:student_login')


def teacher_logout_view(request):
    logout(request)
    return redirect('custom_auth_app:teacher_login')


def admin_logout_view(request):
    logout(request)
    return redirect('cadmin:admin_login')
