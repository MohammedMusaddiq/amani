from tkinter import Place
from django import forms
from .models import Assignment, StudyMaterial, Announcement


class DateInput(forms.DateInput):
    input_type = 'date'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['branch', 'semester', 'subject', 'assignment_name', 'assignment_description',
                  'assignment_file', 'assignment_deadline', 'assignment_status']

        widgets = {
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch'}),
            'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Semester'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'assignment_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assignment Name'}),
            'assignment_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Assignment Description'}),
            'assignment_file': forms.FileInput(
                attrs={'class': 'form-control', 'placeholder': 'Assignment File'}),
            'assignment_deadline': DateInput(attrs={'class': 'form-control', }),
            'assignment_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assignment Status'}),
        }


class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['branch', 'semester', 'subject', 'study_material_name', 'study_material_description',
                  'study_material_file']

        widgets = {
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch'}),
            'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Semester'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'study_material_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Study Material Name'}),
            'study_material_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Study Material Description'}),
            'study_material_file': forms.FileInput(
                attrs={'class': 'form-control', 'placeholder': 'Study Material File'}),
        }
