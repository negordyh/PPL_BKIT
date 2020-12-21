

##a.Use list comprehension approach
# b. Use recursive approach
# c. Use high-order function approach?


def double_a(lst):
    return [x*2 for x in lst]
def double_b(lst):
    if (lst==[]):
        return []
    else:
        return [lst[0] * 2] + double_b(lst[1:])
def double_c(lst):
    return list(map(lambda x:x*2,lst))

lst = [5,7,12,-4]       ## [10, 14, 24, -8] 
print(double_a(lst))
print(double_b(lst))
print(double_c(lst))


