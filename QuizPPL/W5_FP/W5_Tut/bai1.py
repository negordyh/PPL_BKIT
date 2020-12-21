lst = [5,7,12,-4]
def double_a(lst):
    return [x * 2 for x in lst]
def double_recursion(arr, double_arr):
    if arr == []:
        return double_arr
    double_arr.append(arr[0] * 2)
    return double_recursion(arr[1:],double_arr)
def double_b(arr):
    double_lst = []
    double_recursion(arr,double_lst)
    return double_lst
    
#high order function
def double_c(lst):    
    return list(map(lambda x: 2*x, lst))
print(double_a(lst))
print(double_b(lst))
print(double_c(lst))