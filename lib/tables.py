__author__ = 'travisselland'

class Table(list):

    headers = [ 'Col1', 'Col2', 'Col3']
    fields = [ 'col1', 'col2', 'col3']
    css_class = 'table table-bordered table-striped'
    rows_per_page = 5

    def __init__(self, qry):
        self.qry = qry

    def paginate(self, request):
        try:
            page = int(request.REQUEST.get('table_page'))
        except ValueError:
            page = 0
        self.qry = self.qry[page * self.rows_per_page: (page + 1) * self.rows_per_page]
        print("inside paginate")

    def __str__(self):
        html =[]
        html.append('<table class="{}">'.format(self.css_class))

        #table headers
        html.append('<tr>')
        for item in self.headers:
            html.append('<th>{}</th>'.format(item))
        html.append('</tr>')

        #table data
        for row in self:
            html.append('<tr>')
            for item in row:
                html.append('<td>{}</td>'.format(item))
            html.append('</tr>')
        html.append('</table>')
        return ''.join(html)