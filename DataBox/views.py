from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello user with ip: %s' % request.META['REMOTE_ADDR'])


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
