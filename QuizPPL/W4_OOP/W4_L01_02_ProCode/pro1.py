from abc import ABC, abstractmethod


class Exp(ABC):
    @abstractmethod
    def eval(self): pass


class IntLit(Exp):

    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num


class UnExp(Exp):
    def __init__(self, operator, arg):
        assert operator in '+-'
        self.operator = operator
        self.arg = arg

    def eval(self):
        v = self.arg.eval()
        v = v if self.operator == '+' else -v
        return v


class BinExp(Exp):
    def __init__(self, left, operator, right):
        assert operator in '+-*/'
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        a = self.left.eval()
        b = self.right.eval()
        if self.operator == '+':
            v = a + b
        elif self.operator == '-':
            v = a - b
        elif self.operator == '*':
            v = a * b
        else:
            v = a / b
        return v

x1 = IntLit(3)
x2 = IntLit(4)
x3 = FloatLit(2.0)
x4 = BinExp(x2, '*', x3)
x5 = BinExp(x1, '+', x4)

print(x5.eval())

