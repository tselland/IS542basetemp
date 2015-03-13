from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from pagination import models as mod
from lib import tables


def pagination(request):
    params = {}

    params['initial_page'] = 0

    return render_to_response('table_demo.html', params)


ROWS_PER_PAGE = 5

def get_table(request):
    try:
        page = int(request.urlparams[0])
    except ValueError:
        page = 0

    qry = mod.User.objects.all()
    qry = qry[page * ROWS_PER_PAGE: (page + 1) * ROWS_PER_PAGE]

    users = UserTable()
    for user in qry:
        users.append([
            user.first_name,
            user.last_name,
            user.email,
        ])


    params = {
        'users':users
    }

    return render_to_response('table_demo.get_table.html', params)

class UserTable(tables.Table):
    headers = ['First Name', 'Last Name', 'Email']