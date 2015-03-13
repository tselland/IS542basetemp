from django.shortcuts import render
from django.shortcuts import render_to_response
from gallery import models as mod

# Create your views here.
def gallery(request):

    images = mod.databaseImage.objects.all()

    params = {
        'images':images,
    }

    return render_to_response('gallery.html', params)