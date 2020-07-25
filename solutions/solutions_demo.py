def sort_list(list):
    list.sort(reverse=True)
    return list


def list_string(list):
    s = ''
    for i in list:
        s += str(i)
    return s


def string_int(s):
    return int(s)
