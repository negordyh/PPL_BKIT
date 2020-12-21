
def lessThan(n, lst):
    return [x for x in lst if x < n]

def lessThan(n, lst):
    if (lst==[]):
        return []
    else:
        if (lst[0]<n):
            return [lst[0]] + lessThan(n,lst[1:])
        else:
            return lessThan(n,lst[1:])

def lessThan(n, lst):
    return list(filter(lambda x:x<n,lst))

# using reduce
# lessThan(50, [1, 55, 6, 2]) returns [1,6,2]
# from functools import reduce
# def lessThan_reduce(n,lst)
#     return reduce(lambda x,y: x+[y] if y<n else x, lst, [])
# print (lessThan_reduce(50, [1, 55, 6, 2]))