from django.forms import ModelForm, TextInput, IntegerField

from .models import Table

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['division', 'subject', 'fiz_face', 'tabel_time']

        widgets = {
            "division": TextInput(attrs={
                "class": "inline-input",
                'placeholder': 'Подразделение'
            }),
            "subject": TextInput(attrs={
                "class": "inline-input",
                'placeholder': 'Сотрудник'
            }),

            "fiz_face": TextInput(attrs={
                "class": "inline-input",
                'placeholder': 'Физическое лицо'
            }),

            "tabel_time": TextInput(attrs={
                "class": "inline-input",
                'placeholder': 'Табель учёта времени'
            }),
        }