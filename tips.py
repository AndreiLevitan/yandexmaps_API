import logging


def all_to_str(non_str_iter):  # приводит список чисел к списку строк через итераторы
    str_iter = list(map(lambda x: str(x), non_str_iter))
    return str_iter


def fetch_to_tuple(*args):  # привождение любого ввода к виду (float, float)
    case = args[0]
    if len(case) == 1:
        case = case[0]
        if isinstance(case, str):
            case = [float(i) for i in case.split()]
        if isinstance(case, list):
            case = tuple([float(i) for i in case])
        elif isinstance(case, tuple):
            pass
        return case
    elif len(case) == 2:
        case = tuple([float(i) for i in case])
        return case
    logging.critical('fetch_to_tuple unable to fetch input: %r', case)
    return None
