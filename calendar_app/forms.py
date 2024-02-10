from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from django import forms
from .models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from datepickerwidget.widgets import DateWidget, DateTimeWidget


class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['owner', ]
        widgets = {
            # Use localization and bootstrap 4
            'start': DateTimeWidget(attrs={'id': "id_end"}, usel10n=False, bootstrap_version=4),
            'end': DateTimeWidget(attrs={'id': "id_end"}, usel10n=False, bootstrap_version=4),
        }
