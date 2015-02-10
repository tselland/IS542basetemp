
from django.shortcuts import render_to_response
from datetime import datetime

current_year = datetime.now().strftime('%Y')

params = {
    'current_year':current_year,
}

def index(request):
    return render_to_response('index.html', params)