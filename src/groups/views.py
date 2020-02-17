from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from groups.models import Group
from groups.forms import GroupsAddForm


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()

    fn = request.GET.get('group_name')
    if fn:
        queryset = queryset.filter(Q(group_name__istartswith=fn) |
                                   Q(group_size__icontains=fn) |
                                   Q(group_email__icontains=fn))

    return render(request,
                  'groups_list.html',
                  context={'groups': queryset})


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})


def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} not found')

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'groups_edit.html',
                  context={'form': form, 'pk': pk})
