"""Write a recursive function that takes a multi-dimensional list, and returns a one-dimensional list. For the love of God, write some tests.
ex1:
input = [1, 2, [3], [4,5]] ## has 3 lists
output = [1, 2, 3, 4, 5]

ex2:
input = [1, [2], [3, [4, 5, [6]]], 7]  ##5 lists
output = [1, 2, 3, 4, 5, 6, 7]
"""


def flatten_list(lst):
    final_list = []
    
    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        final_list = final_list + flatten_list(lst[0])
        if isinstance(lst[1], list):
            final_list = final_list + flatten_list(lst[1])
        return final_list

    elif isinstance(lst[0], int):
        final_list.append(lst[0])
        print(final_list)
        if len(lst) == 1:
            return final_list
    return final_list + flatten_list(lst[1:])



   




# input = [1, 2, [3], [4,5]]
input = [1, [2], [3, [4, 5, [6]]], 7]
print(flatten_list(input))