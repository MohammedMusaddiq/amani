from django.shortcuts import redirect, render

from custom_auth_app.models import Student, Teacher
from sta.forms import AssignmentForm, StudyMaterialForm, AnnouncementForm
from sta.models import Assignment, StudyMaterial, Announcement
from .decorators import student_required, teacher_required


# student views

@student_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    context = {
        'title': 'Student Dashboard',
        'navbar_active': 'student_dashboard',
        'student': student,
    }
    return render(request, 'sta/student_dashboard.html', context)


@student_required
def stu_assignments(request):
    user = request.user
    student = Student.objects.get(user=user)
    assignments = Assignment.objects.filter(semester__icontains=student.semester)
    context = {
        'title': 'Student Assignments',
        'navbar_active': 'StuAssignments',
        'assignments': assignments,
    }
    return render(request, 'sta/stu_assignments.html', context)


@student_required
def stu_study_material(request):
    user = request.user
    student = Student.objects.get(user=user)
    study_materials = StudyMaterial.objects.filter(semester__icontains=student.semester)
    context = {
        'title': 'Student Study Material',
        'navbar_active': 'StuStudyMaterial',
        'study_materials': study_materials,
    }
    return render(request, 'sta/stu_study_material.html', context)


@student_required
def stu_question_forum(request):
    context = {
        'title': 'Student Question Forum',
        'navbar_active': 'StuQuestionsForum',
    }
    return render(request, 'sta/stu_question_forum.html', context)


@student_required
def seat_allotment(request):
    context = {
        'title': 'Seat Allotment',
        'navbar_active': 'SeatAllotments',
    }
    return render(request, 'sta/seat_allotment.html', context)


@student_required
def stu_announcements(request):
    user = request.user
    student = Student.objects.get(user=user)
    announcements = Announcement.objects.filter(semester__icontains=student.semester)
    context = {
        'title': 'Student Announcements',
        'navbar_active': 'StuAnnouncements',
        'announcements': announcements,
    }
    return render(request, 'sta/stu_announcements.html', context)


# teacher views

@teacher_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    context = {
        'title': 'Teacher Dashboard',
        'navbar_active': 'teacher_dashboard',
        'teacher': teacher,
    }
    return render(request, 'sta/teacher_dashboard.html', context)


@teacher_required
def tea_assignments(request):
    user = request.user
    assignments = Assignment.objects.filter(teacher=user)
    context = {
        'title': 'Teacher Assignments',
        'navbar_active': 'TeaAssignments',
        'assignments': assignments,
    }
    return render(request, 'sta/tea_assignments.html', context)


@teacher_required
def create_assignment(request):
    teacher = request.user
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.teacher = teacher
            f.save()
            return redirect('sta:tea_assignments')
        else:
            print(form.errors)
    context = {
        'title': 'Student Assignments',
        'navbar_active': 'TeaAssignments',
        'form': form,
    }
    return render(request, 'sta/create_assignments.html', context)


@teacher_required
def edit_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    form = AssignmentForm(instance=assignment)
    if request.method == 'POST':
        form = AssignmentForm(request.POST or None, request.FILES or None, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('sta:tea_assignments')
    context = {
        'title': 'Update Assignment',
        'navbar_active': 'TeaAssignments',
        'form': form,
        'assignment': assignment,
    }
    return render(request, 'sta/tea_edit_assignment.html', context)


@teacher_required
def delete_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    assignment.delete()
    return redirect('sta:tea_assignments')


@teacher_required
def tea_study_material(request):
    user = request.user
    study_materials = StudyMaterial.objects.filter(teacher=user)
    context = {
        'title': 'Teacher Study Material',
        'navbar_active': 'TeaStudyMaterial',
        'study_materials': study_materials,
    }
    return render(request, 'sta/tea_study_material.html', context)


@teacher_required
def create_study_material(request):
    form = StudyMaterialForm()
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.teacher = request.user
            f.save()
            return redirect('sta:tea_study_material')
        else:
            print(form.errors)
    context = {
        'title': 'Create Study Material',
        'navbar_active': 'TeaStudyMaterial',
        'form': form,
    }
    return render(request, 'sta/create_studymaterial.html', context)


@teacher_required
def edit_study_material(request, pk):
    study_material = StudyMaterial.objects.get(pk=pk)
    form = StudyMaterialForm(instance=study_material)
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST or None, request.FILES or None, instance=study_material)
        if form.is_valid():
            form.save()
            return redirect('sta:tea_study_material')
    context = {
        'title': 'Edit Study Material',
        'navbar_active': 'TeaStudyMaterial',
        'study_material': study_material,
        'form': form,
    }
    return render(request, 'sta/edit_studymaterial.html', context)


@teacher_required
def delete_study_material(request, pk):
    study_material = StudyMaterial.objects.get(pk=pk)
    study_material.delete()
    return redirect('sta:tea_study_material')


@teacher_required
def tea_question_forum(request):
    context = {
        'title': 'Teacher Questions Forum',
        'navbar_active': 'TeaQuestionsForum',
    }
    return render(request, 'sta/tea_question_forum.html', context)


@teacher_required
def tea_announcements(request):
    user = request.user
    announcements = Announcement.objects.filter(teacher=user)
    context = {
        'title': 'Teacher Announcements',
        'navbar_active': 'TeaAnnouncements',
        'announcements': announcements,
    }
    return render(request, 'sta/tea_announcements.html', context)


@teacher_required
def create_announcement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.teacher = request.user
            f.save()
            return redirect('sta:tea_announcements')
        else:
            print(form.errors)
    context = {
        'title': 'Create Announcement',
        'navbar_active': 'TeaAnnouncements',
        'form': form,
    }
    return render(request, 'sta/create_announcement.html', context)


@teacher_required
def edit_announcement(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    form = AnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST or None, request.FILES or None, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('sta:tea_announcements')
    context = {
        'title': 'Edit Announcement',
        'navbar_active': 'TeaAnnouncements',
        'announcement': announcement,
        'form': form,
    }
    return render(request, 'sta/edit_announcement.html', context)


@teacher_required
def delete_announcement(request, pk):
    announcement = Announcement.objects.get(pk=pk)
    announcement.delete()
    return redirect('sta:tea_announcements')
