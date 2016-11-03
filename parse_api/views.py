# coding:utf-8
"""
报告解析API
"""
from parse_api.forms import UploadFileForm
from django.conf import settings
from django.http import JsonResponse
import time


def handle_uploaded_file(fp, title, file_type):
    if file_type == UploadFileForm.PDF:
        file_type = 'pdf'
    elif file_type == UploadFileForm.HTML:
        file_type = 'html'
    elif file_type == UploadFileForm.MHT:
        file_type = 'mht'
    elif file_type == UploadFileForm.WORD:
        file_type = 'word'
    else:
        file_type = 'pdf'
    file_path = settings.UPLOAD_DIR + file_type + '/' + title + str(
        time.time()) + '.' + file_type
    # 文件大于20MB返回错误
    if fp.size >= 20*1024*1024:
        return None
    with open(file_path, 'wb+') as destination:
        for chunk in fp.chunks():
            destination.write(chunk)
    return file_path


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            fp = form.cleaned_data['fp']
            file_type = form.cleaned_data['file_type']
            result = handle_uploaded_file(fp, title, file_type)
        if result:
            return JsonResponse(data={'success': True,
                                      'msg': 'file upload success'})
        else:
            return JsonResponse(data={'success': False,
                                      'msg': 'file is too larger'})
    else:
        return JsonResponse(data={'success': False,
                                  'msg': 'Error'})


def parse_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            fp = form.cleaned_data['fp']
            file_type = form.cleaned_data['file_type']
            result = handle_uploaded_file(fp, title, file_type)
        if result:
            return JsonResponse(data={'success': True,
                                      'msg': 'file upload success'})
        else:
            return JsonResponse(data={'success': False,
                                      'msg': 'file is too larger'})
    else:
        return JsonResponse(data={'success': False,
                                  'msg': 'Error'})