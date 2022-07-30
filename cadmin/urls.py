from django.urls import path

from . import views

app_name = 'cadmin'

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('students_list/', views.students_list, name='students_list'),
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('admin_seat_allotments/', views.admin_seat_allotments, name='admin_seat_allotments'),
    path('create_teacher_account/', views.create_teacher_account, name='create_teacher_account'),
    path('create_student_account/', views.create_student_account, name='create_student_account'),
    path('delete/teacher/<int:idx>/', views.delete_teacher, name='delete_teacher'),
    path('delete/student/<int:idx>/', views.student_delete, name='student_delete'),
]
