# coding:utf-8
from django.conf.urls import url
from parse_api.views import upload_file

urlpatterns = [url(r'^upload_file/$', upload_file, name='upload_file')
               ]
