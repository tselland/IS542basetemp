from django.shortcuts import render_to_response
from django import forms
from datetime import date
from django.forms import widgets
from django.template import RequestContext
from django.forms.formsets import formset_factory
from lib.forms import ForecastForm
from lib.widgets import DatePickerWidget


def friday(request):
    # EventFormset = formset_factory(EventForm, extra=1)
    # AnnouncementFormset = formset_factory(AnnouncementForm, extra=1)
    #initial forecast form doesn't need a formset.
    forecastForm = mainForm(request)
    if request.method == "POST":
        # eventFormset = EventFormset(request.POST)
        # announcementFormset = AnnouncementFormset(request.POST)
        print('insidepost')
        if(forecastForm.is_valid() ): #& eventFormset.is_valid() & announcementFormset.is_valid()):
            #on submit, the message gets translated to the new template
            message = forecastForm.cleaned_data['message']
        else:
            message = "Error: Message was not transferred"

        return render_to_response('forecast_output.html',
                {'forecastForm': forecastForm, 'message': message},
                context_instance=RequestContext(request))

    forecastParams = {
        'forecastForm': forecastForm,
        # 'eventFormset': EventFormset(),
        # 'announcementFormset':AnnouncementFormset(),
    }
    return render_to_response('friday.html', forecastParams, context_instance=RequestContext(request))

class mainForm(ForecastForm):
    def init(self):
        # self.fields['message'] = forms.CharField(label="Reid's Message", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['date'] = forms.DateTimeField(widget=DatePickerWidget)


#Basic Forecast Template
    #Message
    #Announcements (Button to add additional)
    #Events (Button to add additional)
    #

#add additional forms for additional events
#add announcements button

