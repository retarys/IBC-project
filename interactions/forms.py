from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from attr import field
from django import forms
from .models import Snippet
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

class ClientsForm(forms.Form):

    interaction_type = forms.ChoiceField(choices=[('event','Event'),('meeting','Meeting')], required=True)
    date = forms.DateField(widget=AdminDateWidget())
    time = forms.TimeField(widget=AdminTimeWidget())
    comment = forms.CharField(widget=forms.Textarea,required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'interaction_type',
            'date',
            'time',
            'comment',
            Submit('sumbit','Submit', css_class = 'btn-success')
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('interaction_type','date','time','comment')
        widgets = {
            'date':AdminDateWidget(),
            'time':AdminTimeWidget(),
        }