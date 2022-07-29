from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Student, Teacher, Subjects


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    verbose_name_plural = 'Teacher'


class UserAdmin(AuthAdmin):
    inlines = [StudentInline, TeacherInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'is_student', 'is_teacher', 'is_active',)
    list_filter = ('username', 'is_student', 'is_teacher', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                    'is_active', 'is_student', 'is_teacher')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active', 'is_student',
                'is_teacher')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, UserAdmin)


class SubjectInline(admin.TabularInline):
    model = Subjects
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'semester', 'roll_no',)
    list_filter = ('user', 'branch', 'semester', 'roll_no',)
    fieldsets = (
        (None, {'fields': ('user', 'branch', 'semester', 'roll_no',)}),
    )
    search_fields = ('user', 'branch', 'semester', 'roll_no',)
    ordering = ('user',)


admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('user', 'branch',)
    list_filter = ('user', 'branch',)
    fieldsets = (
        (None, {'fields': ('user', 'branch',)}),
    )
    search_fields = ('user', 'branch',)
    ordering = ('user',)


admin.site.register(Teacher, TeacherAdmin)

admin.site.register(Subjects)
