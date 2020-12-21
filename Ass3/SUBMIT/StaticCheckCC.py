
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        listvardecl=[]
        listfuncdecl=[]
        for x in ast.decl:
            if type(x)==VarDecl:
                listvardecl.append(x)
            else:
                listfuncdecl.append(x)

        evm=reduce(lambda a,b: a + [self.visit(b, a)], listvardecl, c)
        for func in listfuncdecl:
            fname=func.name.name
            for x in evm:
                if fname==x.name:
                    raise Redeclared(Function(), fname)

            param=[]
            for i in range(len(func.param)):
                if func.param[i].varDimen!=[]:
                    param.append(ArrayType(func.param[i].varDimen,Unknown()))
                else:
                    param.append(Unknown())
            evm.append(Symbol(fname,MType(param,Unknown())))

        [self.visit(x,evm) for x in listfuncdecl]

        main_func=0
        for x in evm:
            if x.name=="main" and type(x.mtype)==MType:
                main_func=1

        if main_func==0:
            raise NoEntryPoint()

    def visitVarDecl(self,ctx:VarDecl,c):
        name=ctx.variable.name
        for x in c:
            if name == x.name:
                raise Redeclared(Variable(),name)

        if ctx.varDimen!=[]:
            if ctx.varInit:
                return Symbol(name,self.visit(ctx.varInit,None))
            return Symbol(name,ArrayType(ctx.varDimen,Unknown()))

        if ctx.varInit:
            return Symbol(name,self.visit(ctx.varInit,None))
        return Symbol(name, Unknown())

    def visitFuncDecl(self,ctx:FuncDecl,c):
        name=ctx.name.name
        #Parameter
        d=[]
        for x in ctx.param:
            for y in d:
                if x.variable.name==y.name:
                    raise Redeclared(Parameter(),x.variable.name)
            if x.varDimen!=[]:
                d.append(Symbol(x.variable.name, ArrayType(x.varDimen,Unknown())))
            else:
                d.append(Symbol(x.variable.name, Unknown()))

        param_type=0
        for x in c:
            if x.name==name and type(x.mtype)==MType:
                param_type=x.mtype.intype
        for i in range(len(param_type)):
            d[i].mtype=param_type[i]

        paramlist = [x.name for x in d]

        #VarDecl
        e=reduce(lambda a, b: a + [self.visit(b, a)], ctx.body[0], d)

        f=[x.name for x in e]

        for x in c:
            if x.name in f:
                pass
            else:
                e.append(x)

        self_func=0
        for x in c:
            if name==x.name and type(x.mtype)==MType:
                self_func=x

        e.append(Symbol("truongdinhduc",self_func.mtype))

        for x in ctx.body[1]:
            if type(x)==Return:
                ft=self.visit(x,e)
                for y in e:
                    if y.name=="truongdinhduc":
                        if type(y.mtype.restype)==Unknown:
                            y.mtype.restype=ft
                        else:
                            if type(ft)!=type(y.mtype.restype):
                                raise TypeMismatchInStatement(x)
            else:
                self.visit(x,e)
                m=0
                for y in e:
                    if y.name==name and type(y.mtype)==MType:
                        m=y
                for z in e:
                    if z.name=="truongdinhduc":
                        if type(z.mtype.restype)==Unknown:
                            z.mtype.restype=m.mtype.restype
                        if type(m.mtype.restype)==Unknown:
                            m.mtype.restype = z.mtype.restype

        for x in e:
            for y in c:
                if x.name==y.name and x.name not in f:
                    c.append(x)
                    c.remove(y)

        functype=Unknown()
        for x in e:
            if x.name=="truongdinhduc":
                if type(x.mtype.restype)!=Unknown:
                    functype=x.mtype.restype
                else:
                    functype=VoidType()

        paramtype=[]
        for i in range(len(paramlist)):
            for x in e:
                if x.name==paramlist[i] and type(x.mtype)!=MType:
                    paramtype.append(x.mtype)

        for x in c:
            if x.name==name and type(x.mtype)==MType:
                c.remove(x)
        c.append(Symbol(name, MType(paramtype,functype)))

    #Return
    def visitReturn(self,ctx:Return,c):
        if ctx.expr:
            return self.visit(ctx.expr,c)
        return VoidType()

    #Assign
    def visitAssign(self,ctx:Assign,c):
        r = self.visit(ctx.rhs, c)
        l = self.visit(ctx.lhs, c)

        if l=="TypeCannotBeInferred" or r=="TypeCannotBeInferred":
            raise TypeCannotBeInferred(ctx)

        if type(l)==Unknown and type(r)==Symbol:
            raise TypeCannotBeInferred(ctx)

        if type(l)==Unknown and type(r)==Unknown:
            raise TypeCannotBeInferred(ctx)

        if type(l)!=ArrayType and type(r)==ArrayType:
            raise TypeMismatchInStatement(ctx)

        if type(l)==ArrayType and type(r)!=ArrayType:
            raise TypeMismatchInStatement(ctx)

        if type(r)==VoidType:
            raise TypeMismatchInStatement(ctx)

        if isinstance(l,Unknown):
            l = r
            if isinstance(ctx.lhs,Id):
                for x in c:
                    if ctx.lhs.name == x.name and type(x.mtype)!=MType:
                        c.append(Symbol(x.name, l))
                        c.remove(x)
            if type(ctx.lhs)==ArrayCell:
                if type(ctx.lhs.arr)==Id:
                    for x in c:
                        if ctx.lhs.arr.name == x.name and type(x.mtype)==ArrayType:
                            c.append(Symbol(x.name,ArrayType(x.mtype.dimen,l)))
                            c.remove(x)
                if type(ctx.lhs.arr)==CallExpr:
                    for x in c:
                        if ctx.lhs.arr.method.name == x.name and type(x.mtype)==MType:
                            x.mtype.restype.eletype=l

        if isinstance(r,Unknown):
            r = l
            if isinstance(ctx.rhs,Id):
                for x in c:
                    if ctx.rhs.name == x.name and type(x.mtype)!=MType:
                        c.append(Symbol(x.name, r))
                        c.remove(x)
            if isinstance(ctx.rhs,ArrayCell):
                for x in c:
                    if ctx.rhs.arr.name == x.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name, ArrayType(x.mtype.dimen, r)))
                        c.remove(x)

        if type(r)==Symbol:
            c.append(Symbol(r.name,MType(r.mtype.intype,l)))
            r = l

        if type(l)!=type(r):
            raise TypeMismatchInStatement(ctx)

        if isinstance(l,ArrayType):
            if l.dimen!=r.dimen:
                raise TypeMismatchInStatement(ctx)

            l_type=l.eletype
            r_type=r.eletype

            if type(l_type)==Unknown and type(r_type)==Unknown:
                raise TypeCannotBeInferred(ctx)

            if type(l_type)==Unknown:
                for x in c:
                    if x.name==ctx.lhs.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name, ArrayType(l.dimen, r_type)))
                        c.remove(x)
                l_type=r_type

            if type(r_type)==Unknown:
                for x in c:
                    if x.name==ctx.rhs.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name,ArrayType(r.dimen, l_type)))
                        c.remove(x)
                r_type=l_type
            if type(l_type)!=type(r_type):
                raise TypeMismatchInStatement(ctx)

    def visitFor(self,ctx:For,c):
        scala = self.visit(ctx.idx1, c)
        e1 = self.visit(ctx.expr1, c)
        if type(scala)==Unknown and type(e1)==Unknown:
            raise TypeCannotBeInferred(ctx)
        if type(scala)==Unknown:
            for x in c:
                if ctx.idx1.name==x.name and type(x.mtype)!=MType:
                    x.mtype=IntType()
            scala=IntType()

        if type(e1)==Unknown:
            if type(ctx.expr1) == Id:
                for x in c:
                    if x.name == ctx.expr1.name and type(x.mtype) != MType:
                        x.mtype = IntType()
            if type(ctx.expr1) == ArrayCell:
                for x in c:
                    if x.name == ctx.expr1.arr.name and type(x.mtype) != MType:
                        x.mtype.eletype = IntType()
            e1 = IntType()
        if type(e1) == Symbol:
            c.append(Symbol(e1.name, MType(e1.mtype.intype, IntType())))
            e1 = IntType()

        e2 = self.visit(ctx.expr2, c)
        if type(e2)==Unknown:
            if type(ctx.expr2) == Id:
                for x in c:
                    if x.name == ctx.expr2.name and type(x.mtype) != MType:
                        x.mtype = BoolType()
            if type(ctx.expr2) == ArrayCell:
                for x in c:
                    if x.name == ctx.expr2.arr.name and type(x.mtype) != MType:
                        x.mtype.eletype = BoolType()
            e2 = BoolType()
        if type(e2) == Symbol:
            c.append(Symbol(e2.name, MType(e2.mtype.intype, BoolType())))
            e2 = BoolType()

        e3 = self.visit(ctx.expr3, c)
        if type(e3)==Unknown:
            if type(ctx.expr3) == Id:
                for x in c:
                    if x.name == ctx.expr3.name and type(x.mtype) != MType:
                        x.mtype = IntType()
            if type(ctx.expr3) == ArrayCell:
                for x in c:
                    if x.name == ctx.expr3.arr.name and type(x.mtype) != MType:
                        x.mtype.eletype = IntType()
            e3 = IntType()
        if type(e3) == Symbol:
            c.append(Symbol(e3.name, MType(e3.mtype.intype, IntType())))
            e3 = IntType()

        listexp=[e1,e2,e3]
        if "TypeCannotBeInferred" in listexp:
            raise TypeCannotBeInferred(ctx)
        if type(scala)!=IntType:
            raise TypeMismatchInStatement(ctx)
        if type(e1)!=IntType:
            raise TypeMismatchInStatement(ctx)
        if type(e2)!=BoolType:
            raise TypeMismatchInStatement(ctx)
        if type(e3)!=IntType:
            raise TypeMismatchInStatement(ctx)

        e=reduce(lambda a, b: a + [self.visit(b, a)], ctx.loop[0], [])
        decl=[x.name for x in e]
        redecl=[x.name for x in c if x.name in decl]

        for x in c:
            if x.name in decl:
                pass
            else:
                e.append(x)

        for x in ctx.loop[1]:
            if type(x) == Return:
                ft = self.visit(x, e)
                for y in e:
                    if y.name == "truongdinhduc":
                        if type(y.mtype.restype) == Unknown:
                            e.append(Symbol("truongdinhduc", MType([], ft)))
                            e.remove(y)
                        else:
                            if type(ft) != type(y.mtype.restype):
                                raise TypeMismatchInStatement(x)
            else:
                self.visit(x, e)

        for x in c:
            if x.name=="truongdinhduc":
                c.remove(x)
        for x in e:
            if x.name == "truongdinhduc":
                c.append(x)

        for x in e:
            for y in c:
                if x.name==y.name and x.name not in redecl:
                    c.append(x)
                    c.remove(y)

    def visitIf(self,ctx:If,c):
        for ifthen in ctx.ifthenStmt:
            expr=self.visit(ifthen[0],c)
            if expr=="TypeCannotBeInferred":
                raise TypeCannotBeInferred(ctx)
            if type(expr)==Unknown:
                if type(ifthen[0])==Id:
                    for x in c:
                        if x.name==ifthen[0].name and type(x.mtype)!=MType:
                            x.mtype=BoolType()
                if type(ifthen[0]) == ArrayCell:
                    for x in c:
                        if x.name==ifthen[0].arr.name and type(x.mtype)!=MType:
                            x.mtype.eletype=BoolType()
                expr=BoolType()
            if type(expr)==Symbol:
                c.append(Symbol(expr.name,MType(expr.mtype.intype,BoolType())))
                expr = BoolType()
            if type(expr)!=BoolType:
                raise TypeMismatchInStatement(ctx)

            e = reduce(lambda a, b: a + [self.visit(b, a)], ifthen[1], [])
            decl = [y.name for y in e]

            for x in c:
                if x.name in decl:
                    pass
                else:
                    e.append(x)

            for x in ifthen[2]:
                if type(x) == Return:
                    ft = self.visit(x, e)
                    for y in e:
                        if y.name == "truongdinhduc":
                            if type(y.mtype.restype) == Unknown:
                                e.append(Symbol("truongdinhduc", MType([], ft)))
                                e.remove(y)
                            else:
                                if type(ft) != type(y.mtype.restype):
                                    raise TypeMismatchInStatement(x)
                else:
                    self.visit(x, e)

            for x in c:
                if x.name == "truongdinhduc":
                    c.remove(x)
            for x in e:
                if x.name == "truongdinhduc":
                    c.append(x)

            for x in e:
                for y in c:
                    if x.name == y.name and x.name not in decl:
                        c.append(x)
                        c.remove(y)

        #Visit Else
        e = reduce(lambda a, b: a + [self.visit(b, a)], ctx.elseStmt[0], [])
        decl = [y.name for y in e]
        redecl = [y.name for y in c if y.name in decl]

        for x in c:
            if x.name in decl:
                pass
            else:
                e.append(x)

        for x in ctx.elseStmt[1]:
            if type(x) == Return:
                ft = self.visit(x, e)
                for y in e:
                    if y.name == "truongdinhduc":
                        if type(y.mtype.restype) == Unknown:
                            e.append(Symbol("truongdinhduc", MType([], ft)))
                            e.remove(y)
                        else:
                            if type(ft) != type(y.mtype.restype):
                                raise TypeMismatchInStatement(x)
            else:
                self.visit(x, e)

        for x in c:
            if x.name == "truongdinhduc":
                c.remove(x)
        for x in e:
            if x.name == "truongdinhduc":
                c.append(x)

        for x in e:
            for y in c:
                if x.name == y.name and x.name not in redecl:
                    c.append(x)
                    c.remove(y)

    def visitDowhile(self,ctx:Dowhile,c):
        e = reduce(lambda a, b: a + [self.visit(b, a)], ctx.sl[0], [])
        decl = [x.name for x in e]

        for x in c:
            if x.name in decl:
                pass
            else:
                e.append(x)

        for x in ctx.sl[1]:
            if type(x) == Return:
                ft = self.visit(x, e)
                for y in e:
                    if y.name == "truongdinhduc":
                        if type(y.mtype.restype) == Unknown:
                            e.append(Symbol("truongdinhduc", MType([], ft)))
                            e.remove(y)
                        else:
                            if type(ft) != type(y.mtype.restype):
                                raise TypeMismatchInStatement(x)
            else:
                self.visit(x, e)

        for x in c:
            if x.name == "truongdinhduc":
                c.remove(x)
        for x in e:
            if x.name == "truongdinhduc":
                c.append(x)

        expr=self.visit(ctx.exp,e)
        if type(expr) == Unknown:
            if type(ctx.exp) == Id:
                for x in e:
                    if x.name == ctx.exp.name and type(x.mtype) != MType:
                        x.mtype = BoolType()
            if type(ctx.exp) == ArrayCell:
                for x in e:
                    if x.name == ctx.exp.arr.name and type(x.mtype) != MType:
                        x.mtype.eletype = BoolType()
            expr = BoolType()
        if type(expr) == Symbol:
            e.append(Symbol(expr.name, MType(expr.mtype.intype, BoolType())))
            expr = BoolType()
        if expr == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ctx)
        if type(expr)!=BoolType:
            raise TypeMismatchInStatement(ctx)

        for x in e:
            for y in c:
                if x.name == y.name and x.name not in decl:
                    c.append(x)
                    c.remove(y)

    def visitWhile(self,ctx:While,c):
        expr = self.visit(ctx.exp,c)
        if type(expr) == Unknown:
            if type(ctx.exp) == Id:
                for x in c:
                    if x.name == ctx.exp.name and type(x.mtype) != MType:
                        x.mtype = BoolType()
            if type(ctx.exp) == ArrayCell:
                for x in c:
                    if x.name == ctx.exp.arr.name and type(x.mtype) != MType:
                        x.mtype.eletype = BoolType()
            expr = BoolType()
        if type(expr) == Symbol:
            c.append(Symbol(expr.name, MType(expr.mtype.intype, BoolType())))
            expr = BoolType()
        if expr == "TypeCannotBeInferred":
            raise TypeCannotBeInferred(ctx)
        if type(expr) != BoolType:
            raise TypeMismatchInStatement(ctx)

        e = reduce(lambda a, b: a + [self.visit(b, a)], ctx.sl[0], [])
        decl = [x.name for x in e]

        for x in c:
            if x.name in decl:
                pass
            else:
                e.append(x)

        for x in ctx.sl[1]:
            if type(x) == Return:
                ft = self.visit(x, e)
                for y in e:
                    if y.name == "truongdinhduc":
                        if type(y.mtype.restype) == Unknown:
                            e.append(Symbol("truongdinhduc", MType([], ft)))
                            e.remove(y)
                        else:
                            if type(ft) != type(y.mtype.restype):
                                raise TypeMismatchInStatement(x)
            else:
                self.visit(x, e)

        for x in c:
            if x.name == "truongdinhduc":
                c.remove(x)
        for x in e:
            if x.name == "truongdinhduc":
                c.append(x)

        for x in e:
            for y in c:
                if x.name == y.name and x.name not in decl:
                    c.append(x)
                    c.remove(y)

    #Id
    def visitId(self,ctx:Id,c):
        for x in c:
            if ctx.name==x.name and type(x.mtype)!=MType:
                return x.mtype
        raise Undeclared(Identifier(),ctx.name)

    #ArrayCell
    def visitArrayCell(self,ctx:ArrayCell,c):
        arr=self.visit(ctx.arr,c)
        if arr=="TypeCannotBeInferred":
            return "TypeCannotBeInferred"
        if not isinstance(arr,ArrayType):
            raise TypeMismatchInExpression(ctx)

        listexpr=[self.visit(x,c) for x in ctx.idx]
        if "TypeCannotBeInferred" in listexpr:
            return "TypeCannotBeInferred"

        for i in range(len(listexpr)):
            if type(listexpr[i])==Unknown:
                if type(ctx.idx[i])==Id:
                    for x in c:
                        if x.name==ctx.idx[i].name:
                            x.mtype=IntType()
                if type(ctx.idx[i])==ArrayCell:
                    for x in c:
                        if x.name==ctx.idx[i].arr.name and type(x.mtype)==ArrayType:
                            x.mtype.eletype=IntType()
                listexpr[i]=IntType()
            if type(listexpr[i])==Symbol:
                c.append(Symbol(listexpr[i].name,MType(listexpr[i].mtype.intype,IntType())))
                listexpr[i]=IntType()

        if len(arr.dimen)!=len(listexpr):
            raise TypeMismatchInExpression(ctx)
        for x in listexpr:
            if not isinstance(x,IntType):
                raise TypeMismatchInExpression(ctx)
        return arr.eletype

    #Exp
    def visitBinaryOp(self, ctx: BinaryOp, c):
        l = self.visit(ctx.left, c)
        if isinstance(l,Unknown):
            if isinstance(ctx.left, Id):
                for x in c:
                    if ctx.left.name == x.name:
                        if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                            c.append(Symbol(x.name, IntType()))
                            l = IntType()
                        if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                            c.append(Symbol(x.name, FloatType()))
                            l = FloatType()
                        if ctx.op in ["&&", "||"]:
                            c.append(Symbol(x.name, BoolType()))
                            l = BoolType()
                        c.remove(x)
            if isinstance(ctx.left, ArrayCell):
                for x in c:
                    if ctx.left.arr.name == x.name:
                        if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen,IntType())))
                            l = IntType()
                        if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen,FloatType())))
                            l = FloatType()
                        if ctx.op in ["&&", "||"]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen,BoolType())))
                            l = BoolType()
                        c.remove(x)
        if type(l) == Symbol:
            if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                c.append(Symbol(l.name, MType(l.mtype.intype, IntType())))
                l = IntType()
            if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                c.append(Symbol(l.name, MType(l.mtype.intype, FloatType())))
                l = FloatType()
            if ctx.op in ["&&", "||"]:
                c.append(Symbol(l.name, MType(l.mtype.intype, BoolType())))
                l = BoolType()

        r = self.visit(ctx.right, c)
        if isinstance(r, Unknown):
            if isinstance(ctx.right, Id):
                for x in c:
                    if ctx.right.name == x.name:
                        if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                            c.append(Symbol(x.name, IntType()))
                            r = IntType()
                        if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                            c.append(Symbol(x.name, FloatType()))
                            r = FloatType()
                        if ctx.op in ["&&", "||"]:
                            c.append(Symbol(x.name, BoolType()))
                            r = BoolType()
                        c.remove(x)
            if isinstance(ctx.right, ArrayCell):
                for x in c:
                    if ctx.right.arr.name == x.name:
                        if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, IntType())))
                            r = IntType()
                        if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, FloatType())))
                            r = FloatType()
                        if ctx.op in ["&&", "||"]:
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, BoolType())))
                            r = BoolType()
                        c.remove(x)
        if type(r) == Symbol:
            if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
                c.append(Symbol(r.name, MType(r.mtype.intype, IntType())))
                r = IntType()
            if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
                c.append(Symbol(r.name, MType(r.mtype.intype, FloatType())))
                r = FloatType()
            if ctx.op in ["&&", "||"]:
                c.append(Symbol(r.name, MType(r.mtype.intype, BoolType())))
                r = BoolType()

        if l=="TypeCannotBeInferred" or r=="TypeCannotBeInferred":
            return "TypeCannotBeInferred"

        if ctx.op in ["+", "-", "*", "\\", "%", "==", "!=", "<", ">", "<=", ">="]:
            if not isinstance(l,IntType) or not isinstance(r,IntType):
                raise TypeMismatchInExpression(ctx)
            if ctx.op in ["==", "!=", "<", ">", "<=", ">="]:
                return BoolType()
            return IntType()

        if ctx.op in ["+.", "-.", "*.", "\\.", "=/=", "<.", ">.", "<=.", ">=."]:
            if not isinstance(l,FloatType) or not isinstance(r,FloatType):
                raise TypeMismatchInExpression(ctx)
            if ctx.op in ["=/=", "<.", ">.", "<=.", ">=."]:
                return BoolType()
            return FloatType()

        if ctx.op in ["&&", "||"]:
            if not isinstance(l,BoolType) or not isinstance(r,BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnaryOp(self, ctx: UnaryOp, c):
        r = self.visit(ctx.body, c)
        if isinstance(r, Unknown):
            if isinstance(ctx.body, Id):
                for x in c:
                    if ctx.body.name == x.name:
                        if ctx.op == "-":
                            c.append(Symbol(x.name, IntType()))
                            r = IntType()
                        if ctx.op == "-.":
                            c.append(Symbol(x.name, FloatType()))
                            r = FloatType()
                        if ctx.op == "!":
                            c.append(Symbol(x.name, BoolType()))
                            r = BoolType()
                        c.remove(x)
            if isinstance(ctx.body, ArrayCell):
                for x in c:
                    if ctx.body.arr.name == x.name:
                        if ctx.op == "-":
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, IntType())))
                            r = IntType()
                        if ctx.op == "-.":
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, FloatType())))
                            r = FloatType()
                        if ctx.op == "!":
                            c.append(Symbol(x.name, ArrayType(x.mtype.dimen, BoolType())))
                            r = BoolType()
                        c.remove(x)
        if type(r) == Symbol:
            if ctx.op =="-":
                c.append(Symbol(r.name, MType(r.mtype.intype, IntType())))
                r = IntType()
            if ctx.op =="-.":
                c.append(Symbol(r.name, MType(r.mtype.intype, FloatType())))
                r = FloatType()
            if ctx.op =="!":
                c.append(Symbol(r.name, MType(r.mtype.intype, BoolType())))
                r = BoolType()

        if r=="TypeCannotBeInferred":
            return "TypeCannotBeInferred"

        if ctx.op == "-":
            if not isinstance(r,IntType):
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if ctx.op == "-.":
            if not isinstance(r,FloatType):
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op == "!":
            if not isinstance(r,BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitCallStmt(self,ctx:CallStmt,c):
        f=0
        for x in c:
            if ctx.method.name == x.name and type(x.mtype)==MType:
                f = x
        if f==0:
            raise Undeclared(Function(),ctx.method.name)

        agru = [self.visit(x, c) for x in ctx.param]
        if len(agru) != len(f.mtype.intype):
            raise TypeMismatchInStatement(ctx)
        if "TypeCannotBeInferred" in agru:
            raise TypeCannotBeInferred(ctx)

        if type(f.mtype.restype)!=Unknown:
            if type(f.mtype.restype)!=VoidType:
                raise TypeMismatchInStatement(ctx)

            for i in range(len(agru)):
                if type(agru[i])==Unknown and type(f.mtype.intype[i])==Unknown:
                    raise TypeCannotBeInferred(ctx)

                if type(agru[i])==ArrayType and type(f.mtype.intype[i])!=ArrayType:
                    raise TypeMismatchInStatement(ctx)
                if type(agru[i])!=ArrayType and type(f.mtype.intype[i])==ArrayType:
                    raise TypeMismatchInStatement(ctx)

                if type(agru[i])==Unknown:
                    if type(ctx.param[i])==Id:
                        for x in c:
                            if x.name==ctx.param[i].name and type(x.mtype)!=MType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)

                    if type(ctx.param[i])==ArrayCell:
                        for x in c:
                            if x.name==ctx.param[i].arr.name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,ArrayType(x.mtype.dimen,f.mtype.intype[i])))
                                c.remove(x)
                    agru[i]=f.mtype.intype[i]

                if type(agru[i])==Symbol:
                    c.append(Symbol(agru[i].name,MType(agru[i].mtype.intype,f.mtype.intype[i])))
                    agru[i] = f.mtype.intype[i]

                if type(f.mtype.intype[i])==Unknown:
                    f.mtype.intype[i]=agru[i]

                if type(agru[i])!=type(f.mtype.intype[i]):
                    raise TypeMismatchInStatement(ctx)

                if type(agru[i] == ArrayType) and type(f.mtype.intype[i]) == ArrayType:
                    if f.mtype.intype[i].dimen != agru[i].dimen:
                        raise TypeMismatchInExpression(ctx)
                    if type(f.mtype.intype[i].eletype) == Unknown and type(agru[i].eletype) == Unknown:
                        return TypeCannotBeInferred(ctx)
                    if type(f.mtype.intype[i].eletype) == Unknown:
                        f.mtype.intype[i].eletype = agru[i].eletype
                    if type(agru[i].eletype) == Unknown:
                        for x in c:
                            if x.name == ctx.param[i].name and type(x.mtype) == ArrayType:
                                c.append(Symbol(x.name, f.mtype.intype[i]))
                                c.remove(x)
                        agru[i] = f.mtype.intype[i]
                    if type(f.mtype.intype[i].eletype) != type(agru[i].eletype):
                        raise TypeMismatchInExpression(ctx)

        #Inference type of function
        if type(f.mtype.restype)==Unknown:
            for x in agru:
                if type(x)==Unknown or type(x)==Symbol:
                    raise TypeCannotBeInferred(ctx)

            for x in c:
                if x.name==ctx.method.name and type(x.mtype)==MType:
                    c.remove(x)
            newfunc=Symbol(ctx.method.name,MType(agru,VoidType()))
            c.append(newfunc)

    def visitCallExpr(self,ctx:CallExpr,c):
        f=0
        for x in c:
            if ctx.method.name==x.name and type(x.mtype)==MType:
                f=x
        if f==0:
            raise Undeclared(Function(),ctx.method.name)

        agru=[self.visit(x,c) for x in ctx.param]

        if len(agru) != len(f.mtype.intype):
            raise TypeMismatchInExpression(ctx)
        if "TypeCannotBeInferred" in agru:
            return "TypeCannotBeInferred"
        if type(f.mtype.restype)!=Unknown:
            for i in range(len(agru)):
                if type(agru[i])==Unknown and type(f.mtype.intype[i])==Unknown:
                    return "TypeCannotBeInferred"
                if type(agru[i])==ArrayType and type(f.mtype.intype[i])!=ArrayType:
                    raise TypeMismatchInExpression(ctx)
                if type(agru[i])!=ArrayType and type(f.mtype.intype[i])==ArrayType:
                    raise TypeMismatchInExpression(ctx)

                if type(agru[i])==Unknown:
                    if type(ctx.param[i])==Id:
                        for x in c:
                            if x.name==ctx.param[i].name and type(x.mtype)!=MType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)

                    if type(ctx.param[i])==ArrayCell:
                        for x in c:
                            if x.name==ctx.param[i].arr.name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,ArrayType(x.mtype.dimen,f.mtype.intype[i])))
                                c.remove(x)
                    agru[i]=f.mtype.intype[i]

                if type(agru[i])==Symbol:
                    c.append(Symbol(agru[i].name,MType(agru[i].mtype.intype,f.mtype.intype[i])))
                    agru[i] = f.mtype.intype[i]

                if type(f.mtype.intype[i])==Unknown:
                    f.mtype.intype[i]=agru[i]

                if type(agru[i])!=type(f.mtype.intype[i]):
                    raise TypeMismatchInExpression(ctx)

                if type(agru[i]==ArrayType) and type(f.mtype.intype[i])==ArrayType:
                    if f.mtype.intype[i].dimen!=agru[i].dimen:
                        raise TypeMismatchInExpression(ctx)
                    if type(f.mtype.intype[i].eletype)==Unknown and type(agru[i].eletype)==Unknown:
                        return "TypeCannotBeInferred"
                    if type(f.mtype.intype[i].eletype) == Unknown:
                        f.mtype.intype[i].eletype=agru[i].eletype
                    if type(agru[i].eletype)==Unknown:
                        for x in c:
                            if x.name==ctx.param[i].name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)
                        agru[i]=f.mtype.intype[i]
                    if type(f.mtype.intype[i].eletype)!=type(agru[i].eletype):
                        raise TypeMismatchInExpression(ctx)

            return f.mtype.restype

        if type(f.mtype.restype) == Unknown:
            for x in agru:
                if type(x)==Unknown:
                    return "TypeCannotBeInferred"

            for x in c:
                if x.name==ctx.method.name and type(x.mtype)==MType:
                    c.remove(x)
            newfunc=Symbol(ctx.method.name,MType(agru,Unknown()))
            return newfunc

    #Literal
    def visitIntLiteral(self, ctx: IntLiteral, c):
        return IntType()

    def visitFloatLiteral(self, ctx: FloatLiteral, c):
        return FloatType()

    def visitStringLiteral(self, ctx: StringLiteral, c):
        return StringType()

    def visitBooleanLiteral(self, ctx: BooleanLiteral, c):
        return BoolType()

    def visitArrayLiteral(self, ctx: ArrayLiteral, c):
        dimen = [len(ctx.value)]
        ele = ctx.value[0]
        while type(ele) == ArrayLiteral:
            dimen.append(len(ele.value))
            ele = ele.value[0]
        return ArrayType(dimen, self.visit(ele, None))

    def visitBreak(self,ctx:Break,c):
        pass

    def visitContinue(self,ctx:Continue,c):
        pass



