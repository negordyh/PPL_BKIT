from functools import reduce
from operator import concat
lst = [[1,2,3],['a','b','c'],[1.1,2.1,3.1],[1],5]
def flatten_a(lst):
    return [val for sublist in lst for val in sublist]
def flatten_b(lst):
    return sum(([x] if not isinstance(x,list) else flatten_b(x) for x in lst), [])
# def flatten_c(lst):
#     return list(reduce(concat,lst,[]))
def flatten_c(lst):
    return reduce(lambda x,y: x + y,lst)

# print(flatten_a(lst))
# print(flatten_b(lst))
print(flatten_c(lst))

# print(sum(([x] for x in [1,2,3]),[]))
