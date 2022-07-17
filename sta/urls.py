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
    path('t/study_material/', views.tea_study_material, name='tea_study_material'),
    path('t/question_forum/', views.tea_question_forum, name='tea_question_forum'),
    path('t/announcements/', views.tea_announcements, name='tea_announcements'),
]
