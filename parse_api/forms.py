# coding:utf-8
from django import forms
"""
    forms 类提供表单验证FORM
"""


class UploadFileForm(forms.Form):
    """上传文件表单"""
    (PDF, MHT, WORD, HTML) = (0, 1, 2, 3)
    title = forms.CharField(max_length=60, min_length=2)
    file_type = forms.IntegerField(max_value=HTML, min_value=PDF)
    fp = forms.FileField(allow_empty_file=False)




