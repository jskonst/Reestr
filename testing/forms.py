from django import forms
from models import testMan
class testForms(forms.ModelForm):
    class Meta:
        model=testMan
    