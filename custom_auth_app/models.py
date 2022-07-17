from sre_constants import BRANCH
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    is_teacher = models.BooleanField(_('is_teacher'), default=False)
    is_student = models.BooleanField(_('is_student'), default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return str(self.user.username)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    branch = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return str(self.user.username)


class Subjects(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.subject
