from django.shortcuts import redirect, render

from custom_auth_app.models import Student, Teacher
from sta.forms import AssignmentForm, StudyMaterialForm
from sta.models import Assignment, StudyMaterial


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
    user = request.user
    student = Student.objects.get(user=user)
    assignments = Assignment.objects.filter(semester__icontains=student.semester)
    context = {
        'title': 'Student Assignments',
        'navbar_active': 'StuAssignments',
        'assignments': assignments,
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
    assignments = Assignment.objects.all()
    context = {
        'title': 'Teacher Assignments',
        'navbar_active': 'TeaAssignments',
        'assignments': assignments,
    }
    return render(request, 'sta/tea_assignments.html', context)


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


def delete_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    assignment.delete()
    return redirect('sta:tea_assignments')


def tea_study_material(request):
    study_materials = StudyMaterial.objects.all()
    context = {
        'title': 'Teacher Study Material',
        'navbar_active': 'TeaStudyMaterial',
        'study_materials': study_materials,
    }
    return render(request, 'sta/tea_study_material.html', context)


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


def delete_study_material(request, pk):
    study_material = StudyMaterial.objects.get(pk=pk)
    study_material.delete()
    return redirect('sta:tea_study_material')


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
