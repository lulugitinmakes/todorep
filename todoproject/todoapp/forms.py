from . models import Task1
from django import forms
class TodoForm(forms.ModelForm):
    class Meta:
        model=Task1
        fields='__all__'