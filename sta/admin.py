from django.contrib import admin

from .models import Assignment, StudyMaterial, Announcement


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'branch', 'semester', 'subject', 'assignment_name', 'assignment_description',
                    'assignment_file', 'assignment_date', 'assignment_deadline', 'assignment_status']
    list_filter = ['assignment_date']
    search_fields = ['teacher', 'branch', 'semester', 'subject', 'assignment_name', 'assignment_description',
                     'assignment_file', 'assignment_date', 'assignment_deadline', 'assignment_status']


admin.site.register(Assignment, AssignmentAdmin)


class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'branch', 'semester', 'subject', 'study_material_name', 'study_material_description',
                    'study_material_file', 'uploaded_date']
    list_filter = ['uploaded_date']
    search_fields = ['teacher', 'branch', 'semester', 'subject', 'study_material_name', 'study_material_description',
                     'study_material_file', 'uploaded_date']


admin.site.register(StudyMaterial, StudyMaterialAdmin)


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'branch', 'semester', 'announcement_name', 'announcement_description',
                    'announcement_date_time']
    list_filter = ['announcement_date_time']
    search_fields = ['teacher', 'branch', 'semester', 'announcement_name', 'announcement_description',
                     'announcement_date_time']


admin.site.register(Announcement, AnnouncementAdmin)
