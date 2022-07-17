from multiprocessing import context
from django.shortcuts import render

from custom_auth_app.models import Student, Teacher


# student views

def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    context = {
        'title': 'Student Dashboard',
        'navbar_active': 'student_dashboard',
        'student': student,
    }
    return render(request, 'sta/student_dashboard.html', context)


def stu_assignments(request):
    context = {
        'title': 'Student Assignments',
        'navbar_active': 'StuAssignments',
    }
    return render(request, 'sta/stu_assignments.html', context)


def stu_study_material(request):
    context = {
        'title': 'Student Study Material',
        'navbar_active': 'StuStudyMaterial',
    }
    return render(request, 'sta/stu_study_material.html', context)


def stu_question_forum(request):
    context = {
        'title': 'Student Question Forum',
        'navbar_active': 'StuQuestionsForum',
    }
    return render(request, 'sta/stu_question_forum.html', context)


def seat_allotment(request):
    context = {
        'title': 'Seat Allotment',
        'navbar_active': 'SeatAllotments',
    }
    return render(request, 'sta/seat_allotment.html', context)


def stu_announcements(request):
    context = {
        'title': 'Student Announcements',
        'navbar_active': 'StuAnnouncements',
    }
    return render(request, 'sta/stu_announcements.html', context)


# teacher views

def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    context = {
        'title': 'Teacher Dashboard',
        'navbar_active': 'teacher_dashboard',
        'teacher': teacher,
    }
    return render(request, 'sta/teacher_dashboard.html', context)


def tea_assignments(request):
    context = {
        'title': 'Teacher Assignments',
        'navbar_active': 'TeaAssignments',
    }
    return render(request, 'sta/tea_assignments.html', context)


def tea_study_material(request):
    context = {
        'title': 'Teacher Study Material',
        'navbar_active': 'TeaStudyMaterial',
    }
    return render(request, 'sta/tea_study_material.html', context)


def tea_question_forum(request):
    context = {
        'title': 'Teacher Questions Forum',
        'navbar_active': 'TeaQuestionsForum',
    }
    return render(request, 'sta/tea_question_forum.html', context)


def tea_announcements(request):
    context = {
        'title': 'Teacher Announcements',
        'navbar_active': 'TeaAnnouncements',
    }
    return render(request, 'sta/tea_announcements.html', context)
