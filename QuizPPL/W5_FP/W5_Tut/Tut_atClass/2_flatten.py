from functools import reduce
from operator import concat
def flatten_a(lst):
    return [y for x in lst for y in x]

def flatten_b(lst):
    if (lst==[]):
        return []
    else:
        return lst[0] + flatten(lst[1:])

def flatten_c(lst):
    return reduce(lambda x,y:x+y,lst)

lst = [[1,2,3],['a','b','c'],[1.1,2.1,3.1],[1],5]
print(flatten_a(lst))
print(flatten_b(lst))
print(flatten_c(lst))
