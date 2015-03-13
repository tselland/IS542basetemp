from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def pagination(request):

    return render_to_response('table_demo.html')