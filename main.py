
from prettytable import PrettyTable
from utils import get_xifi_hash, statistical_median, statistical_mode


def parse_str_list(elements: list):

    result = []

    for el in elements:
        if el.count('.') == 1:
            result.append(float(el.strip()))
        else:
            result.append(int(el.strip()))

    return result


def create_frecuency_table(elements: list):

    table = PrettyTable()
    table.field_names = ('xi', 'fi', 'hi', 'Fi', 'Hi', 'xifi')

    if len(elements) == 0:
        return table

    hash_xifi = get_xifi_hash(elements)
    n = len(elements)
    Fi = 0
    Hi = 0

    for xi, fi in hash_xifi.items():

        Fi += fi
        hi = (fi/n)
        Hi += hi
        xifi = xi*fi

        data_row = (xi, fi, round(hi, 2), Fi, round(Hi, 2), xifi)
        table.add_row(data_row)

    xifi_summation = sum([xi*fi for xi, fi in hash_xifi.items()])

    total_row = ('total', n, 1, '', '', xifi_summation)
    table.add_row(list(' '*6))
    table.add_row(total_row)

    mean = round(sum(elements) / n, 2)
    mode = statistical_mode(elements)
    median = statistical_median(elements)

    table.add_row(('mean:', mean, '', '', '', ''))
    table.add_row(('mode:', mode, '', '', '', ''))
    table.add_row(('median:', median, '', '', '', ''))

    return table


try:
    values = parse_str_list(input('Write list of numbers:').split(','))
    print(values)
    table = create_frecuency_table(values)

    print(table)

except Exception as e:
    print("Only numbers can be entered.", e)
