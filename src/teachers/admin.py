from django.contrib import admin

from teachers.models import Teacher
from teachers.forms import TeacherAdminForm


class TeacherAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'email', 'telephone')
    list_select_related = ('group',)
    form = TeacherAdminForm


admin.site.register(Teacher, TeacherAdmin)
