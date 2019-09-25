from django.forms import ModelForm
from django.contrib.admin import widgets

from .models import Event, Category, Account


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ["host", "title", "location", "venue", "start_time", "end_time", "categories"]
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime,
        }


class AccountForm(ModelForm):
    # first_name    = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": }))
    class Meta:
        model = Account
        fields = ["first_name", "surname", "email"]
