def all_to_str(non_str_iter):  # приводит список чисел к списку строк через итераторы
    str_iter = list(map(lambda x: str(x), non_str_iter))
    return str_iter


def fetch_to_tuple(*args):  # привождение любого ввода к виду (float, float)
    case = args[0]
    if len(case) == 2:
        if isinstance(case, str):
            case = [float(i) for i in case.split()]
    elif len(case) == 1:
        case = case[0]
        if isinstance(case, list):
            case = tuple(case)
        elif isinstance(case, tuple):
            pass
    if isinstance(case, tuple):
        return case

    print('Incorrect fetch input: {}'.format(case))
    return None