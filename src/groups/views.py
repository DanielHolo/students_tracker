from django.http import HttpResponse
from django.shortcuts import render

from groups.models import Group


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def groups(request):
    queryset = Group.objects.all()
    response = ''

    fn = request.GET.get('group_name')
    if fn:
        queryset = queryset.filter(group_name__istartswith=fn)

    for group in queryset:
        response += group.get_info() + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})
