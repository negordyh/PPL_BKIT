from functools import reduce
lst = [1, 55, 6, 2]
num = 10
def lessThan_a(num,lst):
    return [x  for x in lst if x < num]
def lessThan_b(num,lst):
    if lst == []:
        return []
    if lst[0] < num:
        return [lst[0]] + lessThan_b(num,lst[1:])
    return lessThan_b(num,lst[1:])
def lessThan_c(num,lst):
    # return list(filter(lambda a: num > a, lst))
    return reduce(lambda x, y: x + [y] if y < num else x,lst,[])

# print(lessThan_a(num,lst))
# print(lessThan_b(num,lst))
print(lessThan_c(num,lst))
