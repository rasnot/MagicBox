from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.template import RequestContext
from django.template.context_processors import csrf
from DataBox.forms import Add_New_Dictionary
from DataBox.models import Dictionary

def hello(request):
    ip = request.META['REMOTE_ADDR']
    return render_to_response('index.html', locals())


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
    if request.method == "POST":
        form = Add_New_Dictionary(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dictionary = Dictionary(name = cd['name'])
            dictionary.save()
            return HttpResponseRedirect(r'index/$')
    else:
        form = Add_New_Dictionary()
    c=locals()
    c.update(csrf(request))
    return render_to_response('add_new_dictionary.html', locals())

#def views_list_of_dictionary