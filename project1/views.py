
from django.shortcuts import render_to_response
from datetime import datetime
import requests

current_year = datetime.now().strftime('%Y')

params = {
    'current_year':current_year,
}

def index(request):

    webID1 = next(request.session.generator)
    webID2 = next(request.session.generator)
    webID3 = next(request.session.generator)
    webID4 = next(request.session.generator)
    webID5 = next(request.session.generator)
    print (webID1, webID2, webID3, webID4, webID5)

    params = {
        'webID1':webID1,
        'webID2':webID2,
        'webID3':webID3,
        'webID4':webID4,
        'webID5':webID5,
    }



    return render_to_response('index.html', params)