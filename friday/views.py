from django.shortcuts import render_to_response
from django import forms
from datetime import date
from django.forms import widgets
from django.template import RequestContext
from django.forms.formsets import formset_factory


def index(request):
    # EventFormset = formset_factory(EventForm, extra=1)
    # AnnouncementFormset = formset_factory(AnnouncementForm, extra=1)

    if request.method == "POST":
        #initial forecast form doesn't need a formset.
        forecastForm = ForecastForm(request.POST)
        # eventFormset = EventFormset(request.POST)
        # announcementFormset = AnnouncementFormset(request.POST)

        if(forecastForm.is_valid() ): #& eventFormset.is_valid() & announcementFormset.is_valid()):

            message = forecastForm.cleaned_data['message']
        else:
            message = "Error: Message was not transferred"

        return render_to_response('forecast_output.html',
                {'forecastForm': forecastForm, 'message': message},
                context_instance=RequestContext(request))

    forecastParams = {
        'forecastForm': ForecastForm(),
        'eventFormset': EventFormset(),
        'announcementFormset':AnnouncementFormset(),
    }
    return render_to_response('friday.html', forecastParams, context_instance=RequestContext(request))

#Basic Forecast Template
    #Message
    #Announcements (Button to add additional)
    #Events (Button to add additional)
    #

#add additional forms for additional events
#add announcements button



class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        days = [(day, day) for day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)]
        months = [(month, month) for month in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')]
        years = [(year, year) for year in (2011, 2012, 2013)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(day=int(datelist[0]), month=int(datelist[1]),
                    year=int(datelist[2]))
        except ValueError:
            return ''
        else:
            return str(D)


