from django.contrib import admin
from DataBox.models import *


class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'dataSet', 'long_name')
    #ordering = ['id',]


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_system')


admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(DictionaryValue)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DataSetAttribute)
admin.site.register(DataSetValue)
