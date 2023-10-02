from django import forms
from .models import emailcheckModel

class emailForm(forms.ModelForm):
    class Meta:
        model=emailcheckModel
        fields=('email',)