from django.forms import forms, ModelForm

from groups.models import Group


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
