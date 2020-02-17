from django.urls import path

from groups.views import generate_group, groups, groups_add, groups_edit

urlpatterns = [
    path('list/', groups, name='groups'),
    path('add/', groups_add, name='groups-add'),
    path('gen/', generate_group, name='gen-grp'),
    path('edit/<int:pk>/', groups_edit, name='groups-edit'),
]
