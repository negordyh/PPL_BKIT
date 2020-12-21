from functools import reduce

# de qui
def mul(lst):
    if lst:
        return lst[0]*mul(lst[1:]) if type(lst[0]) == int else 1*mul(lst[1:])
    else:
    	return 1
print(mul([1.2,5,2,"asd",5.6,6]))
# FB
def mul_int(lst):
	lst_int = list(filter(lambda x: ,lst))
        return x*1 for x in lst_int

print(mul([1.2,5,2,"asd",5.6,6]))