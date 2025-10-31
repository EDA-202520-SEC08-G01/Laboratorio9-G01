from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False


def default_compare_higher_value(father_node, child_node):
    
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False


def new_heap(is_min_pq=True):

    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": default_compare_lower_value if is_min_pq else default_compare_higher_value
    }
    
    al.add_last(heap["elements"], None)
    
    return heap


def priority(my_heap, parent, child):

    return my_heap["cmp_function"](parent, child)


def swim(my_heap, pos):

    while pos > 1:
        parent_pos = pos // 2

        current_element = al.get_element(my_heap["elements"], pos)
        parent_element = al.get_element(my_heap["elements"], parent_pos)

        if priority(my_heap, parent_element, current_element):
            break

        al.change_info(my_heap["elements"], pos, parent_element)
        al.change_info(my_heap["elements"], parent_pos, current_element)
        
        pos = parent_pos


def insert(my_heap, priority_value, value):
    new_entry = pqe.new_pq_entry(priority_value, value)

    al.add_last(my_heap["elements"], new_entry)

    my_heap["size"] += 1

    swim(my_heap, my_heap["size"])
    
    return my_heap


def is_empty(my_heap):
    return my_heap["size"] == 0