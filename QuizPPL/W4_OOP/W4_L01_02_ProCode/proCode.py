from abc import ABC, abstractmethod


class Exp(ABC):
    @abstractmethod
    def eval(self): pass

    @abstractmethod
    def printPrefix(): pass

class IntLit(Exp):

    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def printPrefix(self): 
        return str(self.num)


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def printPrefix(self):
        return str(self.num)


class UnExp(Exp):
    def __init__(self, operator, arg):
        assert operator in '+-'
        self.operator = operator
        self.arg = arg

    def eval(self):
        v = self.arg.eval()
        v = v if self.operator == '+' else -v
        return v

    def printPrefix(self):
        return self.operator + '. ' + self.arg.printPrefix()


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

    def printPrefix(self):
        return self.operator + ' ' + self.left.printPrefix() + ' ' + self.right.printPrefix()

# x1 = IntLit(3)
# x2 = IntLit(4)
# x3 = FloatLit(2.0)
# x4 = BinExp(x2, '*', x3)
# x5 = BinExp(x1, '+', x4)

subFour = UnExp('-', IntLit(4))
threeMultwo = BinExp(IntLit(3), '*', IntLit(2))
result = BinExp(subFour, '+', threeMultwo)
print(result.printPrefix())
