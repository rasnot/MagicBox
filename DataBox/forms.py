# -*- coding: utf-8 -*-
from django import forms
from DataBox.models import Dictionary


class Add_New_Dictionary(forms.Form):
    name = forms.CharField(max_length=100, label='Название словаря:')
    system_dict = forms.BooleanField(label='Системный ли словарь?', required=False)
    type = forms.ChoiceField(label='Тип', choices=((('str', 'str'), ('int', 'int'))))

    def clean_name(self):
        name = self.cleaned_data['name']
        from_db_dict = Dictionary.objects.filter(name = name)
        if len(from_db_dict)>0:
            raise forms.ValidationError("Такой словарь уже существует!")
        return name



class DataSetForm(forms.Form):
    long_name = forms.CharField(max_length=512, label='Довга назва DataSet:')
    short_name = forms.CharField(max_length=256, label='Скорочена назва DataSet:', required=False)
    country_id = forms.IntegerField(required=False)
    region_id = forms.IntegerField(required=False)


