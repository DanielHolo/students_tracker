from django.urls import path

from teachers.views import generate_teacher, teachers, teachers_add, teachers_edit, teacher_contact

urlpatterns = [
    path('list/', teachers, name='teachers'),
    path('add/', teachers_add, name='teachers-add'),
    path('gen/', generate_teacher, name='gen-teach'),
    path('edit/<int:pk>/', teachers_edit, name='teachers-edit'),
    path('contact/', teacher_contact, name='teacher-contact'),
]
