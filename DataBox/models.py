from __future__ import unicode_literals

from django.db import models



class Dictionary(models.Model):
    """Модель для роботи із словниками"""
    #pid = models.IntegerField(blank=True, null=True) #parent id, ????
    name = models.CharField(max_length=256)
    is_system = models.BooleanField(default=False)
    uid = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(default=1)
    user_id = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dictionary'

    def __unicode__(self):
        return self.name


class DictionaryValue(models.Model):
    """Модель для роботи із значеннями словників"""
    dictionary = models.ForeignKey(Dictionary, db_column='dict_id')
    #pid = models.IntegerField(null=True)
    value = models.CharField(max_length=512)
    text_fild1 = models.CharField(max_length=512, blank=True)
    text_fild2 = models.CharField(max_length=512, blank=True)
    text_fild3 = models.CharField(max_length=512, blank=True)
    num_fild1 = models.DecimalField(max_digits=16, decimal_places=5, blank=True, null=True)
    num_fild2 = models.DecimalField(max_digits=16, decimal_places=5, blank=True, null=True)
    num_fild3 = models.DecimalField(max_digits=16, decimal_places=5, blank=True, null=True)
    num_fild4 = models.DecimalField(max_digits=16, decimal_places=5, blank=True, null=True)
    date_fild1 = models.DateTimeField(blank=True, null=True)
    date_fild2 = models.DateTimeField(blank=True, null=True)
    date_fild3 = models.DateTimeField(blank=True, null=True)
    bool_fild1 = models.NullBooleanField(blank=True)
    bool_fild2 = models.NullBooleanField(blank=True)
    bool_fild3 = models.NullBooleanField(blank=True)
    uid = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dictionary_value'

    def __unicode__(self):
        return self.value


class DataSet(models.Model):
    """Модель для роботи із DataSet-ами та їхніми таблицями"""
    pid = models.IntegerField(blank=True, null=True)    # parent id, от кого зависит
    long_name = models.CharField(max_length=512)
    short_name = models.CharField(max_length=256, blank=True)
    country_id = models.ForeignKey(
        DictionaryValue,
        null=True,
        db_column='dict_country_id',
        related_name='dict_country_id')    # поле при'язки до країни
    region_id = models.ForeignKey(
        DictionaryValue,
        null=True,
        db_column='dict_region_id',
        related_name='dict_region_id')      # поле прив'язки до регіону(обл)
    uid = models.IntegerField(blank=True, null=True)        # id таблицы, для реализации языка
    language_id = models.IntegerField(default=1)
    user_id = models.IntegerField(blank=True, null=True)    # кто создал
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dataset'

    def __unicode__(self):
        return self.long_name


class DataSetAttribute(models.Model):
    """Модель для створення атрибутів DataSet"""
    #pid = models.IntegerField(null=True)
    dataSet = models.ForeignKey(DataSet, db_column='dataset_id')    # id таблицы с данными
    dictionary = models.ForeignKey(Dictionary, null=True, db_column='dict_id')    # якщо значення береться із довідника
    long_name = models.CharField(max_length=512)
    short_name = models.CharField(max_length=256)
    column = models.ForeignKey(DictionaryValue, db_column='dict_column_info_id')  # тип колонки char, int, bool...
    uid = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)    # в случае изменения
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dataset_attribute'

    def __unicode__(self):
        return self.dataSet.long_name


class DataSetValue(models.Model):
    """Модель для роботи із значеннями DataSet"""
    dataSet = models.ForeignKey(DataSet, db_column='dataset_id')
    value = models.TextField()
    uid = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField

    class Meta:
        db_table = 'dataset_value'

    def __unicode__(self):
        return self.dataSet.long_name
