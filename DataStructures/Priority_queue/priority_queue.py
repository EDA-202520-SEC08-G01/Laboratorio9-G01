import pq_entry as pe
import DataStructures.List.array_list as al


def default_compare_lower_value(a, b):
    """
    Retorna True si la prioridad a < b (MinPQ)
    """
    return a < b


def default_compare_higher_value(a, b):
    """
    Retorna True si la prioridad a > b (MaxPQ)
    """
    return a > b

def new_heap(is_min_pq=True):
    elements = al.new_list()
    al.add_last(elements, None) 

    if is_min_pq:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value

    pq = {
        "elements": elements,
        "size": 0,
        "cmp_function": cmp_function
    }
    return pq
