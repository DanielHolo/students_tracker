from django.urls import path

from students.views import generate_student, students, students_add, students_edit,contact


urlpatterns = [
    path('list/', students, name='students'),
    path('add/', students, name='students-add'),
    path('gen/', generate_student, name='gen-stud'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
]