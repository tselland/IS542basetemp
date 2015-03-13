__author__ = 'travisselland'

class Table(list):

    headers = [ 'col1', 'col2', 'col3']

    def __str__(self):
        html =[]
        html.append('<table class="table table-bordered table-striped">')

        html.append('<tr>')
        for item in self.headers:
            html.append('<th>{}</th>'.format(item))
        html.append('</tr>')

        for row in self:
            html.append('<tr>')
            for item in row:
                html.append('<td>{}</td>'.format(item))
            html.append('</tr>')
        html.append('</table>')
        return ''.join(html)