from __future__ import unicode_literals

from django.db import models



#название словаря
class Dictionary(models.Model):
    #pid = models.IntegerField(null=True) #parent id, ????
    name = models.CharField(max_length=256)
    is_system = models.BooleanField(default=False)
    uid = models.IntegerField(null=True)
    language_id = models.IntegerField(default=1)
    user_id = models.IntegerField(null=True)
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dictionary'


class DictionaryValue(models.Model):
    dictionary = models.ForeignKey(Dictionary, db_column='dict_id')
    pid = models.IntegerField(null=True)
    long_name = models.CharField(max_length=512)
    short_name = models.CharField(max_length=256, blank=True)
    uid = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dictionary_value'


#название dataseta, и его зависящих таблиц
class DataSet(models.Model):
    pid = models.IntegerField(null=True) #parent id, от кого зависит
    long_name = models.CharField(max_length=512)
    short_name = models.CharField(max_length=256, blank=True)
    uid = models.IntegerField(null=True) #id таблицы, для реализации языка
    language_id = models.IntegerField(default=1)
    user_id = models.IntegerField(null=True) #кто создал
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dataset'


class DataSetAttribute(models.Model):
    #pid = models.IntegerField(null=True)
    dataSet = models.ForeignKey(DataSet, db_column='dataset_id') #id таблицы с данными
    dictionary = models.ForeignKey(Dictionary, null=True, db_column='dict_id') #если колонка ссылается на табл
    long_name = models.CharField(max_length=512)
    short_name = models.CharField(max_length=256, blank=True)
    column = models.ForeignKey(ColumnInfo, db_column='column_info_id') #тип колонки char, int, bool...
    uid = models.IntegerField(null=True)
    language_id = models.IntegerField(default=1)
    user_id = models.IntegerField(null=True) #в случае изменения
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dataset_attribute'


