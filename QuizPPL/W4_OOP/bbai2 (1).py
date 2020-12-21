from abc import ABC, abstractmethod
class Exp(ABC):
    @abstractmethod
    def eval(self):
        pass
    def printPrefix(self):
        pass
class IntLit(Exp):
    def __init__(self,num):
        self.num = num
    def eval(self):
        return self.num
    def printPrefix(self):
        return str(self.num)
class FloatLit(Exp):
    def __init__(self,num):
        self.num = num
    def eval(self):
        return self.num
    def printPrefix(self):
        return str(self.num)
class BinExp(Exp):
    def __init__(self,num1,operator,num2):
        assert operator in '+-*/'
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def eval(self):
        left = self.num1.eval()
        right = self.num2.eval()
        if self.operator == '+':
            return left + right
        if self.operator == '-':
            return left - right
        if self.operator == '/':
            return left / right
        if self.operator == '*':
            return left * right
    def printPrefix(self):
        str = self.operator + ' ' + self.num1.printPrefix() + ' ' + self.num2.printPrefix()
        return str
class UnExp(Exp):
    def __init__(self,operator,num):
        assert operator in '+-'
        self.operator = operator
        self.num = num
    def eval(self):
        operant = self.num.eval()
        if self.operator == '+':
            return operant
        if self.operator == '-':
            return 0 - operant
    def printPrefix(self):
        str = self.operator +'. '+ self.num.printPrefix()
        return str

x1 = IntLit(3)
x2 = IntLit(4)
x3 = BinExp(x1,'*',x1)
x4 = BinExp(x3,'-',x2)
print (x4.printPrefix())
