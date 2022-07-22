from django.urls import path
from . import views

app_name = 'sta'

urlpatterns = [
    # student endpoints
    path('s/', views.student_dashboard, name='student_dashboard'),
    path('s/assignments/', views.stu_assignments, name='stu_assignments'),
    path('s/study_material/', views.stu_study_material, name='stu_study_material'),
    path('s/question_forum/', views.stu_question_forum, name='stu_question_forum'),
    path('s/seat_allotment/', views.seat_allotment, name='seat_allotment'),
    path('s/announcements/', views.stu_announcements, name='stu_announcements'),
    # teacher endpoints
    path('t/', views.teacher_dashboard, name='teacher_dashboard'),
    path('t/assignments/', views.tea_assignments, name='tea_assignments'),
    path('t/assignments/create/', views.create_assignment, name='create_assignment'),
    path('t/assignments/edit/<int:pk>/', views.edit_assignment, name='edit_assignment'),
    path('t/assignments/delete/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('t/study_material/', views.tea_study_material, name='tea_study_material'),
    path('t/study_material/create/', views.create_study_material, name='create_study_material'),
    path('t/study_material/edit/<int:pk>/', views.edit_study_material, name='edit_study_material'),
    path('t/study_material/delete/<int:pk>/', views.delete_study_material, name='delete_study_material'),
    path('t/question_forum/', views.tea_question_forum, name='tea_question_forum'),
    path('t/announcements/', views.tea_announcements, name='tea_announcements'),
    path('t/announcements/create/', views.create_announcement, name='create_announcement'),
    path('t/announcements/edit/<int:pk>/', views.edit_announcement, name='edit_announcement'),
    path('t/announcements/delete/<int:pk>/', views.delete_announcement, name='delete_announcement'),
]
