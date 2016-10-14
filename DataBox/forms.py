# -*- coding: utf-8 -*-
from django import forms


class Add_New_Dictionary(forms.Form):
    name = forms.CharField(max_length=100, label='Название словаря:')
    system_dict = forms.BooleanField(label='Системный ли словарь?', required=False)





