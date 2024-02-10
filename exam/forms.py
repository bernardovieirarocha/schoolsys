from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from django import forms
from .models import Content,Exam
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from datepickerwidget.widgets import DateWidget,DateTimeWidget


class ExamForm(ModelForm):

    class Meta:
        model = Exam
        ordering = ['-id']
        exclude = ['owner', ]
        widgets = {
            #Use localization and bootstrap 4
            'start': DateTimeWidget(attrs={'name': "start"}, usel10n=False, bootstrap_version=4),
            'end': DateTimeWidget(attrs={'id': "id_end"}, usel10n=False, bootstrap_version=4),
            'warning_date':DateWidget(attrs={'id':"yourdatetimeid"}, usel10n = False, bootstrap_version=4)
        }
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Fieldset('Add Content',
                    Formset('skills'),css_class='content'),
                )
            )

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['skill','learning_objects']

SkillFormSet = inlineformset_factory(Exam,Content,form=ContentForm, extra=1,fields=['skill','learning_objects'],can_delete=True)
