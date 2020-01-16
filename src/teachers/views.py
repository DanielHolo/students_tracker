from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from teachers.models import Teacher


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(Q(first_name__icontains=fn) |
                                   Q(last_name__icontains=fn) |
                                   Q(email__icontains=fn))

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
