from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from custom_auth_app.models import Student, Teacher, User, Subjects
from sta.decorators import admin_required
from .forms import AdminLoginForm, TeacherCreateForm, SubjectForm, StudentCreateForm


def admin_login(request):
    form = AdminLoginForm()
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                messages.success(request, f'Welcome {user.username}')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('cadmin:admin_dashboard', )
            else:
                messages.error(request, 'Invalid username or password')
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('cadmin:admin_login')
    context = {
        'navbar_active': 'admin_login',
        'title': 'admin login',
        'form': form,
    }
    return render(request, 'cadmin/admin_login.html', context)


@admin_required
def admin_dashboard(request):
    teachers = Teacher.objects.all().order_by('user')
    context = {
        'navbar_active': 'admin_dashboard',
        'title': 'admin dashboard',
        'teachers': teachers,
    }
    return render(request, 'cadmin/admin_dashboard.html', context)


@admin_required
def students_list(request):
    students = Student.objects.all().order_by('user')
    context = {
        'navbar_active': 'students_list',
        'title': 'students list',
        'students': students,
    }
    return render(request, 'cadmin/students_list.html', context)


@admin_required
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('user')
    context = {
        'navbar_active': 'teachers_list',
        'title': 'teachers list',
        'teachers': teachers,
    }
    return render(request, 'cadmin/teachers_list.html', context)


@admin_required
def admin_seat_allotments(request):
    context = {
        'navbar_active': 'admin_seat_allotments',
        'title': 'admin seat allotments',
    }
    return render(request, 'cadmin/admin_seat_allotments.html', context)


@admin_required
def create_teacher_account(request):
    t_form = TeacherCreateForm()
    sub_form = SubjectForm()
    if request.method == 'POST':
        t_form = TeacherCreateForm(request.POST)
        sub_form = SubjectForm(request.POST)
        try:
            if t_form.is_valid() and sub_form.is_valid():
                subjects = request.POST.getlist('subject_name')
                semester = request.POST.getlist('semester')
                sub_sem = list(zip(subjects, semester))
                username = t_form.cleaned_data['name']
                password = t_form.cleaned_data['password']
                branch = t_form.cleaned_data['branch']
                if Teacher.objects.filter(user__username=username, branch__iexact=branch).exists():
                    messages.error(request, 'Teacher already exists')
                    return redirect('cadmin:create_teacher_account')
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user.is_teacher = True
                user.save()
                teacher = Teacher.objects.create(
                    user=user,
                    branch=branch,
                )
                for item in sub_sem:
                    Subjects.objects.create(
                        teacher=teacher,
                        semester=item[1],
                        subject=item[0],
                    )
                messages.success(request, f'Teacher account created for {username}')
                return redirect('cadmin:teacher_list')
            else:
                messages.error(request, 'Invalid form data')
                return redirect('cadmin:create_teacher_account')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('cadmin:create_teacher_account')
    context = {
        'navbar_active': 'teachers_list',
        'title': 'create teacher account',
        't_form': t_form,
        'sub_form': sub_form,
    }
    return render(request, 'cadmin/create_teacher_account.html', context)


@admin_required
def create_student_account(request):
    s_form = StudentCreateForm()
    if request.method == 'POST':
        s_form = StudentCreateForm(request.POST)
        try:
            if s_form.is_valid():
                username = s_form.cleaned_data['name']
                password = s_form.cleaned_data['password']
                branch = s_form.cleaned_data['branch']
                semester = s_form.cleaned_data['semester']
                roll_no = s_form.cleaned_data['usn']
                if Student.objects.filter(user__username=username, branch__iexact=branch,
                                          roll_no__iexact=roll_no).exists():
                    messages.error(request, 'Student already exists')
                    return redirect('cadmin:create_student_account')
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                user.is_student = True
                user.save()
                Student.objects.create(
                    user=user,
                    branch=branch,
                    semester=semester,
                    roll_no=roll_no,
                )
                messages.success(request, f'Student account created for {username}')
                return redirect('cadmin:students_list')
            else:
                messages.error(request, 'Invalid form data')
                return redirect('cadmin:create_student_account')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('cadmin:create_student_account')
    context = {
        'navbar_active': 'students_list',
        'title': 'create student account',
        's_form': s_form,
    }
    return render(request, 'cadmin/create_student_account.html', context)


def delete_teacher(request, idx):
    try:
        teacher = Teacher.objects.get(id=idx)
        teacher.user.delete()
        teacher.delete()
        messages.success(request, f'Teacher account deleted for {teacher.user.username}')
        return redirect('cadmin:teacher_list')
    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('cadmin:teacher_list')


def student_delete(request, idx):
    try:
        student = Student.objects.get(id=idx)
        student.user.delete()
        student.delete()
        messages.success(request, f'Student account deleted for {student.user.username}')
        return redirect('cadmin:students_list')
    except Exception as e:
        messages.error(request, f'Error: {e}')
        return redirect('cadmin:students_list')
