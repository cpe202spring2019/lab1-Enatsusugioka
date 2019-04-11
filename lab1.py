
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if len(int_list) == 0:
        raise ValueError('empty list')
    elif len(int_list) == 1:
        return int_list[0]
    else:
        max = int_list[0]
        for i in range(1, len(int_list), 1):
            if int_list[i] >= max:
                max = int_list[i]
        return max

def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if len(int_list) == 0:
        raise ValueError('empty list')
    elif len(int_list) == 1:
        return [int_list[0]]
    else:
        return [int_list[-1]] + reverse_rec(int_list[0 : -1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    middle = (high + low) // 2
    if len(int_list) == 0:
        raise ValueError('empty list')
    elif target == int_list[middle]:
        return int_list[middle]
    elif high == low + 1:
        if target == int_list[high]:
            return int_list[high]
        else:
            return None
    elif low == high:
        return None
    elif target > int_list[middle]:
        return bin_search(target, middle, high, int_list)
    else:
        return bin_search(target, low, middle, int_list)
