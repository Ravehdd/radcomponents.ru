from django import forms
from .models import *

import sqlite3
cat = Replace.objects.filter(pk=1)

choices = (
    ('option1', 'Вариант 1'),
    ('option2', 'Вариант 2'),
    ('option3', 'Вариант 3'),
)


class SelectDeviceForm(forms.Form):
    name = forms.CharField(label="Select device name")
    device_need = forms.IntegerField(label="Select amount")
    # category = forms.CharField(required=False)


class ReplaceComponent(forms.Form):
    replacement_choice = forms.ModelChoiceField(queryset=Replace.objects.all(), label="Select other element")
