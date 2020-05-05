from django import forms

from app_main.models import *


class DataDGAForm(forms.ModelForm):

    class Meta:
        model = DataDGA
        fields = (
            'transformer',
            'data_dga'
        )