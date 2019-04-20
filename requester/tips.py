def all_to_str(non_str_iter):  # приводит список чисел к списку строк через итераторы
    str_iter = list(map(lambda x: str(x), non_str_iter))
    return str_iter