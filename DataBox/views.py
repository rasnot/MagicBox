from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from DataBox.models import *
import datetime
from .forms import Add_New_Dictionary


def hello(request):
    ip = request.META['REMOTE_ADDR']
    return render_to_response('index.html', locals())


def datasets(request):
    ds = DataSet.objects.filter(is_table=False)
    return render_to_response('datasets.html', locals())


def dataset(request, id):
    ds = DataSet.objects.filter(id=id)[0]
    tables = DataSet.objects.filter(dataSet=id)
    return render_to_response('dataset.html', locals())

def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())  # locals() -> {'current_date': now}

def add_dictionary(request):
    form = Add_New_Dictionary()
    return render_to_response('add_new_dictionary.html', {'form': form})