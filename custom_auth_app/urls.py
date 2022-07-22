from django.urls import path

from . import views

app_name = 'custom_auth_app'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('logout/', views.logout_view, name='logout'),
]
