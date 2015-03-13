from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.


def pagination(request):
    params = {}

    params['initial_page'] = 5

    return render_to_response('table_demo.html', params)


ROWS_PER_PAGE = 5

def get_table(request):
    try:
        page = int(request.urlparams[0])
    except ValueError:
        page = 0

    users = []
    for i in range(page * ROWS_PER_PAGE, (page+1) * ROWS_PER_PAGE):
        users.append([
            'user %s' % i,
            'FirstName %s' % i,
            'LastName %s' % i,
            'email %s' % i,
        ])


    params = {
        'users':users
    }

    return render_to_response('table_demo.get_table.html', params)

