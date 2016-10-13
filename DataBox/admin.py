from django.contrib import admin
from DataBox.models import *


class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'dataSet', 'long_name')
    #ordering = ['id',]


admin.site.register(Dictionary)
admin.site.register(DictionaryValue)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(DataSetAttribute)
admin.site.register(DataSetValue)
