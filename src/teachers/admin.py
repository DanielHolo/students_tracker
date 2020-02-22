from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'email', 'group')
    list_select_related = ('group',)


admin.site.register(Teacher, TeacherAdmin)
