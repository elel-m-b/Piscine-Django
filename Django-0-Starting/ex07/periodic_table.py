import sys

def parse_file(filename):
    elements = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            name, rest = line.split(' = ')
            data = rest.split(', ')
            element = {'name': name}

            for item in data:
                key, value = item.split(':')
                element[key] = value.strip()

            elements.append(element)

    return elements


def generate_html(elements):
    table = []
    current_row = [''] * 18
    last_position = -1

    for el in elements:
        position = int(el['position'])
        if position <= last_position:
            table.append(current_row)
            current_row = [''] * 18

        cell = (
            '<td style="border:1px solid black;padding:10px;text-align:center;">'
            '<h4>{}</h4>'
            '<ul>'
            '<li>No {}</li>'
            '<li>{}</li>'
            '<li>{}</li>'
            '</ul>'
            '</td>'
        ).format(
            el['name'],
            el['number'],
            el['small'],
            el['molar']
        )

        current_row[position] = cell
        last_position = position

    if current_row:
        table.append(current_row)

    html = '<!DOCTYPE html>\n'
    html += '<html><head><meta charset="utf-8"><title>Periodic Table</title></head><body>\n'
    html += '<table style="border-collapse:collapse;">\n'

    for row in table:
        html += '<tr>'
        for cell in row:
            html += cell or '<td></td>'
        html += '</tr>\n'

    html += '</table></body></html>'
    return html



def periodic_table():
    elements = parse_file('periodic_table.txt')
    html = generate_html(elements)

    with open('periodic_table.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    periodic_table()
