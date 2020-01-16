from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from groups.models import Group
from groups.forms import GroupsAddForm


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()
    response = ''

    fn = request.GET.get('group_name')
    if fn:
        queryset = queryset.filter(group_name__istartswith=fn |
                                   Q(group_size__icontains=fn) |
                                   Q(group_email__icontains=fn))

    for group in queryset:
        response += group.get_info() + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})
