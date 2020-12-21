from abc import ABC, abstractmethod
class Visitor(ABC):
    @abstractmethod
    def visit_int(self,IntLit):
        None
    def visit_float(self,FloatLit):
        None
    def visit_binexp(self,BinExp):
        None
    def  visit_unexp(self,UnExp):
        None

class FloatLit():
    def __init__(self,num):
        self.num = num
    def accept(self, visitor : Visitor):
        return visitor.visit_float(self)
class IntLit():
    def __init__(self,num):
        self.num = num
    def accept(self, visitor : Visitor):
        return visitor.visit_int(self)
class BinExp():
    def __init__(self,num1,operator,num2):
        assert operator in '+-*/'
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def accept(self, visitor : Visitor):
        return visitor.visit_binexp(self)   

class UnExp():
    def __init__(self,operator,num):
        assert operator in '+-'
        self.operator = operator
        self.num = num
    def accept(self, visitor : Visitor):
        return visitor.visit_unexp(self)

class Eval(Visitor):
    def visit_int(self,intLit : IntLit):
        return intLit.num
    def visit_float(self,floatlit : FloatLit):
        return floatlit.num
    def visit_binexp(self,binExp : BinExp):
        left = binExp.num1.acccept(Eval())
        right = binExp.num2.accept(Eval())
        if binExp.operator == '+':
            return left + right
        if binExp.operator == '-':
            return left - right
        if binExp.operator == '/':
            return left / right
        if binExp.operator == '*':
            return left * right
    def visit_unexp(self, unExp : UnExp):
        operant = unExp.num.accept(Eval())
        if unExp.operator == '+':
            return operant
        if unExp.operator == '-':
            return 0 - operant

class PrintPrefix(Visitor):
    def visit_int(self,intLit : IntLit):
        return str(intLit.num)
    def visit_float(self,floatlit : FloatLit):
        return str(floatlit.num)
    def visit_binexp(self,binExp : BinExp):
        str = binExp.operator + ' ' + binExp.num1.accept(PrintPrefix()) + ' ' + binExp.num2.accept(PrintPrefix())
        return str
    def visit_unexp(self, unExp : UnExp):
        str = unExp.operator +'. '+ unExp.num.accept(PrintPrefix())
        return str

class PrintPostfix(Visitor):
    def visit_int(self,intLit : IntLit):
        return str(intLit.num)
    def visit_float(self,floatlit : FloatLit):
        return str(floatlit.num)
    def visit_binexp(self,binExp : BinExp):
        str = binExp.num1.accept(PrintPostfix()) + ' ' + binExp.num2.accept(PrintPostfix()) + ' '+ binExp.operator
        return str
    def visit_unexp(self, unExp : UnExp):
        str = unExp.num.accept(PrintPrefix()) + ' '+ unExp.operator + '.'
        return str

x1 = IntLit(3)
x2 = IntLit(4)
x3 = BinExp(x1,'*',x1)
x4 = BinExp(x3,'-',x2)
print(x4.accept(PrintPostfix()))
