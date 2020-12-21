from functools import reduce
def compose(*arg):
    if arg:
        return lambda x: args[0](compose(*arg[1:])(x))
    else:
        return lambda x: x
def compose(*arg):
    def a(x):
        return reduce(lambda e,f: f(e),list(arg)[::-1],x)
    return a
