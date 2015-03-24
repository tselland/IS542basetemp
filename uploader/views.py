from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
import os.path

def uploader(request):
    params = {}

    form = UploaderForm()
    if request.method == 'POST':
        form = UploaderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['upload_fullname'])
            print('form submitted successfully')
            form = UploaderForm()

    params['form'] = form

    return render_to_response('uploader.html', params)



class UploaderForm(forms.Form):
    name = forms.CharField()
    upload_fullname = forms.CharField(widget=forms.HiddenInput)
    upload_file = forms.FileField(required=False)


def upload(request):
    fullname = os.path.join('/tmp/uploaded_files', request.FILES['upload'].name)

    return HttpResponse(fullname)