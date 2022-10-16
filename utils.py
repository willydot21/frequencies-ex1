
def get_xifi_hash(elements: list):

    simplified_hash = {}

    for xi in elements:
        fi = elements.count(xi)
        simplified_hash[xi] = fi

    return simplified_hash


def statistical_median(elements: list):

    elements.sort()
    n = len(elements)
    median_index = round(n / 2)

    if len(elements) == 1:
        return 1

    if ((n % 2) != 0):
        return elements[median_index]

    a, b = elements[median_index], elements[median_index+1]

    return round((a + b) / 2, 2)


def statistical_mode(elements: list):

    xifi_hash = get_xifi_hash(elements)
    fi_list = xifi_hash.values()
    max_fi = max(fi_list)
    mode = []

    for xi, fi in xifi_hash.items():
        if fi == max_fi:
            mode.append(str(xi))

    if len(mode) == 1:
        return mode[0]

    if len(mode) > 1:
        return f'{mode[0]} - {mode[len(mode)-1]}'
