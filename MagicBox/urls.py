"""MagicBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from DataBox.views import *

urlpatterns = [
    url(r'^$', hello),
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', display_meta),
    url(r'^datasets/$', get_objects, {'template_name': 'datasets.html'}),
    url(r'^dataset/(\d+)/$', dataset),
    url(r'^dictionaries/$', get_objects, {'template_name': 'dictionaries.html'}),
    url(r'^dictionary/(\d+)/$', dictionary),
    url(r'^add_dictionary/$', add_dictionary),
    url(r'^add_dataset/$', add_dataset),
    url(r'^delete_dataset/(\d+)/$', delete_dataset),

    url(r'^dataset_jq/$', dataset_jq),
    url(r'^dataset_grid/$', dataset_grid_handler, name='dataset_grid_handler'),
    url(r'^dataset_grid/cfg/$', dataset_grid_config, name='dataset_grid_config'),
    url(r'^dict_grid/$', dict_grid_handler, name='dict_grid_handler'),
    url(r'^dict_grid/cfg/$', dict_grid_config, name='dict_grid_config'),
    # url(r'^dict_val_grid/$', dict_val_grid_handler, name='dict_val_grid_handler'),
    url(r'^dict_val_grid/(\d+)/$', dict_val_grid_handler, name='dict_val_grid_handler'),
    url(r'^dict_val_grid/cfg/$', dict_val_grid_config, name='dict_val_grid_config'),
]
