#a using recursive
def compose(*arg):
    def h(args):
        return reduce(lambda x, y: y(x), reversed(arg), args)
    return h


#b using high order function

from functools import reduce
def compose(*arg):
    def h(args):
        return reduce(lambda x, y: y(x), reversed(arg), args)
    return h
def square(x):
    return x * x
def increase(x):
    return x + 1
def double(x):
    return x * 2
# print(compose( square,increase,double)(5))
f = compose(increase,square)
print(f(3)) #increase(square(3)) = 10
