from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from DataBox.models import *
import datetime
import json
from django.template import RequestContext
from django.template.context_processors import csrf
from DataBox.forms import *
from DataBox.models import Dictionary


def hello(request):
    ip = request.META['REMOTE_ADDR']
    return render_to_response('index.html', locals())


def get_objects(request, template_name):
    """Отримання всіх DataSet або словників"""
    if template_name == 'datasets.html':
        ds = DataSet.dataset_objects.all()
    if template_name == 'dictionaries.html':
        d = Dictionary.objects.all()
    return render_to_response(template_name, locals())


def dataset(request, id):
    """Відображення конкретного DataSet"""
    ds = DataSet.objects.get(id=id)
    tables = DataSet.objects.filter(dataSet=id)
    return render_to_response('dataset.html', locals())


def dictionary(request, id):
    """Відображення конкретного словника"""
    d = Dictionary.objects.get(id=id)
    dv = DictionaryValue.objects.filter(dictionary=id)
    return render_to_response('dictionary.html', locals())


def add_dictionary(request):
    if request.method == "POST":
        form = Add_New_Dictionary(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dictionary = Dictionary(name=cd['name'])
            dictionary.save()
            return HttpResponseRedirect(r'index/')
    else:
        form = Add_New_Dictionary()
    c = locals()
    c.update(csrf(request))
    return render_to_response('add_new_dictionary.html', locals())


def add_dataset(request):
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ds = DataSet(long_name=cd['long_name'], short_name=cd['short_name'], date_create=datetime.datetime.now())
            ds.save()
            return HttpResponseRedirect(r'/datasets/')
    else:
        form = DataSetForm()
    locals().update(csrf(request))
    return render_to_response('add_dataset.html', locals())


def delete_dataset(request, id):
    """
        Видалення DataSet
        :param id: id DataSet для видалення
    """
    ds = DataSet.objects.get(id=id)
    ds_t = DataSet.table_objects.filter(dataSet=ds.id)
    data = {'is_delete': False}
    if ds_t.__len__() == 0:
        ds.delete()
        data['is_delete'] = True
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps(data), content_type="application/json")
