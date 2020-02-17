from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from teachers.forms import TeachersAddForm, TeacherContactForm
from teachers.models import Teacher


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(Q(first_name__icontains=fn) |
                                   Q(last_name__icontains=fn) |
                                   Q(email__icontains=fn))

    return render(request,
                  'teachers_list.html',
                  context={'teachers': queryset})


def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})


def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Student with id {pk} not found')

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


def teacher_contact(request):
    if request.method == 'POST':
        form = TeacherContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher-contact'))
    else:
        form = TeacherContactForm()

    return render(request,
                  'teachers_contact.html',
                  context={'form': form})
