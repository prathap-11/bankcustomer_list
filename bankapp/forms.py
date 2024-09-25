from .models import bank_tbl
from django import forms

class demo_form(forms.ModelForm):
    class Meta:
        model=bank_tbl
        fields="__all__"