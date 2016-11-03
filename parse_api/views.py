# coding:utf-8
"""
报告解析API
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from parse_api.forms import UploadFileForm
from django.conf import settings


def handle_uploaded_file(fp, title, file_type):
    file_path = settings.UPLOAD_DIR + type + '/' + title + '.' + file_type
    with open(file_path, 'wb+') as destination:
        for chunk in fp.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.fp, form.title, form.file_type)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})