from django.urls import path

from . import views

app_name = 'custom_auth_app'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('student_logout/', views.student_logout_view, name='student_logout'),
    path('teacher_logout/', views.teacher_logout_view, name='teacher_logout'),
    path('admin_logout/', views.admin_logout_view, name='admin_logout'),
]
