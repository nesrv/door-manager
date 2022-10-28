from django import forms

from .models import *


class AddHistory(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = History
        fields = '__all__'


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['door'].empty_label = "Door not selected"

    class Meta:
        model = User
        # fields = ['name', 'login', 'door_id']
        fields = '__all__'

    # name = forms.CharField(max_length=50)
    # login = forms.CharField(max_length=50)
    # door = forms.ModelChoiceField(queryset=Door.objects.all(), empty_label="Door not selected")
