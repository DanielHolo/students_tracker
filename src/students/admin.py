from django.contrib import admin

from students.models import Student
from students.forms import StudentAdminForm


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'email', 'group', 'telephone')
    list_select_related = ('group',)
    form = StudentAdminForm


admin.site.register(Student, StudentAdmin)
