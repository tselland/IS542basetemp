__author__ = 'travisselland'

from django import forms
import django.utils.html as htmlUtil
from basetemp import middleware

class ForecastForm(forms.Form):
    """ Base forecast form. This information will be submitted regardless of the number of events or announcements. """

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.form_id = next(request.session.generator)
        print (self.form_id)
        #init of the Forms Super Class
        super().__init__(*args, **kwargs)
        #specialized init method used only for this form
        self.init()

    def __str__(self):
        return self.as_full()

    def init(self):
        pass

    def commit(self):
        pass

    def as_full(self):
        "Returns this form rendered as HTML with form tags"
        saveButton = '<input class="btn btn-default" type="submit" value="Save"/>'
        html = []
        html.append('<form>')
        html.append('<div class="input-group">')
        for field in self.fields:
            html.append('<input type="text" class="form-control datepicker" placeholder="mm-dd-yy" aria-describedby="date-addon"/>')
        html.append(saveButton)
        html.append('</div>')
        html.append('</form>')
        return htmlUtil.format_html(''.join(html))

    # message = forms.CharField(label="Reid's Message", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    #
    # def clean_message(self):
    #     data = self.cleaned_data['message']
    #     if data == '':
    #         raise forms.ValidationError('Message Field Empty')
    #     return data


class UploaderForm(forms.Form):
    name = forms.CharField()
    upload_fullname = forms.CharField(widget=forms.HiddenInput)
    upload_file = forms.FileField(required=False)



''' These are other forms that I plan on integrating with this outside project, but they are beyond the scope of the current project '''
# class EventForm(forms.Form):
#     """ Form for adding additional events to the Friday Forecast"""
#     eTitle = forms.CharField(label="Event Title", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     date = DateSelectorWidget()
#     time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
#     location = forms.CharField(label="Event Location", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     eDescription = forms.CharField(label="Event Description", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
#
#     def __init__(self, request, *args, **kwargs):
#         request = self.request
#
#         super().__init__()
#
# class AnnouncementForm(forms.Form):
#     """ Form for adding announcments to the forecast """
#     aTitle = forms.CharField(label="Announcement Title", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     aDescription = forms.CharField(label="Announcement Description", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
