from django.contrib import admin

from groups.models import Group
from students.models import Student


class GroupAdmin(admin.ModelAdmin):
    pass


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    inlines = (StudentInline,)


admin.site.register(Group, GroupAdmin)