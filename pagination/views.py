from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from pagination import models as mod
from lib.tables import Table


def pagination(request):
    params = {}

    params['initial_page'] = 0
    return render_to_response('table_demo1.html', params)


def get_table(request):
    params = {}

    users = UserTable(mod.User.objects.all())
    print("<<<<<<<<<<<<<<<<", users.__str__())
    users.paginate(request)

    params['table'] = users

    return render_to_response('tabledemo.get_table.html', params)

class UserTable(Table):
    headers = ['First Name', 'Last Name', 'Email']
    fields = ['first_name', 'last_name', 'email']