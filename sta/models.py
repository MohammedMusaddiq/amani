from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_upload_to(instance, filename):
    return f'{instance.teacher.username}/{filename}'


class Assignment(models.Model):
    ASSIGNMENT_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assignments')
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    assignment_name = models.CharField(max_length=100)
    assignment_description = models.TextField()
    assignment_file = models.FileField(upload_to=get_upload_to, blank=True, null=True)
    assignment_date = models.DateTimeField(auto_now_add=True)
    assignment_deadline = models.DateTimeField()
    assignment_status = models.CharField(
        max_length=100, choices=ASSIGNMENT_STATUS)

    class Meta:
        ordering = ['-assignment_date']
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.assignment_name


class StudyMaterial(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='study_materials')
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    study_material_name = models.CharField(max_length=100)
    study_material_description = models.TextField()
    study_material_file = models.FileField(upload_to=get_upload_to)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_date']
        verbose_name = 'Study Material'
        verbose_name_plural = 'Study Materials'

    def __str__(self):
        return self.study_material_name


class Announcement(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='announcements')
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    announcement_name = models.CharField(max_length=100)
    announcement_description = models.TextField()
    announcement_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-announcement_date_time']
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.announcement_name
