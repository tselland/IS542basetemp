from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
import os.path
from lib.forms import UploaderForm

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

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    f = request.FILES['upload']
    fullname = os.path.join('/tmp/uploaded_files', f.name)

    with open(fullname, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return HttpResponse(fullname)