# -*- coding: utf-8 -*-
from django import forms


class Add_New_Dictionary(forms.Form):
    name = forms.CharField(max_length=100, label='Название словаря:')
    system_dict = forms.BooleanField(label='Системный ли словарь?', required=False)


class DataSetForm(forms.Form):
    long_name = forms.CharField(max_length=512, label='Довга назва DataSet:')
    short_name = forms.CharField(max_length=256, label='Скорочена назва DataSet:', required=False)
    country_id = forms.IntegerField(required=False)
    region_id = forms.IntegerField(required=False)


