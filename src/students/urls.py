from django.urls import path

from students.views import generate_student, students, students_add, students_edit, contact, register, custom_login, activate

urlpatterns = [
    path('list/', students, name='students'),
    path('add/', students_add, name='students-add'),
    path('gen/', generate_student, name='gen-stud'),
    path('edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),

    path('register/', register, name='register'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate,
         name='activate'),
    path('login/', custom_login, name='login'),
]
