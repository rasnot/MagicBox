from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime


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
