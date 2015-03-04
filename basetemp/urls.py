from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'project1.views.index'),
    url(r'^friday', 'friday.views.friday'),
    url(r'^gallery', 'gallery.views.gallery'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Adapted from: http://stackoverflow.com/questions/5517950/django-media-url-and-media-root
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
)
