from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from students.models import Student
from students.forms import StudentsAddForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)

    for student in queryset:
        response += student.get_info() + '<br>'
    return render(request,
                  'students_list.html',
                  context={'students_list': response})


def students_add(request):

    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form})
