
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

    def visitVarDecl(self,ast,c):
        name=ast.variable.name
        for x in c:
            if name == x.name:
                raise Redeclared(Variable(),name)

        if ast.varDimen!=[]:
            if ast.varInit:
                return Symbol(name,self.visit(ast.varInit,None))
            return Symbol(name,ArrayType(ast.varDimen,Unknown()))

        if ast.varInit:
            return Symbol(name,self.visit(ast.varInit,None))
        return Symbol(name, Unknown())

    def visitFuncDecl(self,ast,c):
        name=ast.name.name
        #Parameter
        d=[]
        for x in ast.param:
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
        e=reduce(lambda a, b: a + [self.visit(b, a)], ast.body[0], d)

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

        e.append(Symbol("mvd",self_func.mtype))

        for x in ast.body[1]:
            if type(x)==Return:
                ft=self.visit(x,e)
                for y in e:
                    if y.name=="mvd":
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
                    if z.name=="mvd":
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
            if x.name=="mvd":
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

    #Assign
    def visitAssign(self,ast,c):
        r = self.visit(ast.rhs, c)
        l = self.visit(ast.lhs, c)

        if l=="TypeCannotBeInferred" or r=="TypeCannotBeInferred":
            raise TypeCannotBeInferred(ast)

        if type(l)==Unknown and type(r)==Symbol:
            raise TypeCannotBeInferred(ast)

        if type(l)==Unknown and type(r)==Unknown:
            raise TypeCannotBeInferred(ast)

        if type(l)!=ArrayType and type(r)==ArrayType:
            raise TypeMismatchInStatement(ast)

        if type(l)==ArrayType and type(r)!=ArrayType:
            raise TypeMismatchInStatement(ast)

        if type(r)==VoidType:
            raise TypeMismatchInStatement(ast)

        if isinstance(l,Unknown):
            l = r
            if isinstance(ast.lhs,Id):
                for x in c:
                    if ast.lhs.name == x.name and type(x.mtype)!=MType:
                        c.append(Symbol(x.name, l))
                        c.remove(x)
            if type(ast.lhs)==ArrayCell:
                if type(ast.lhs.arr)==Id:
                    for x in c:
                        if ast.lhs.arr.name == x.name and type(x.mtype)==ArrayType:
                            c.append(Symbol(x.name,ArrayType(x.mtype.dimen,l)))
                            c.remove(x)
                if type(ast.lhs.arr)==CallExpr:
                    for x in c:
                        if ast.lhs.arr.method.name == x.name and type(x.mtype)==MType:
                            x.mtype.restype.eletype=l

        if isinstance(r,Unknown):
            r = l
            if isinstance(ast.rhs,Id):
                for x in c:
                    if ast.rhs.name == x.name and type(x.mtype)!=MType:
                        c.append(Symbol(x.name, r))
                        c.remove(x)
            if isinstance(ast.rhs,ArrayCell):
                for x in c:
                    if ast.rhs.arr.name == x.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name, ArrayType(x.mtype.dimen, r)))
                        c.remove(x)

        if type(r)==Symbol:
            c.append(Symbol(r.name,MType(r.mtype.intype,l)))
            r = l

        if type(l)!=type(r):
            raise TypeMismatchInStatement(ast)

        if isinstance(l,ArrayType):
            if l.dimen!=r.dimen:
                raise TypeMismatchInStatement(ast)

            l_type=l.eletype
            r_type=r.eletype

            if type(l_type)==Unknown and type(r_type)==Unknown:
                raise TypeCannotBeInferred(ast)

            if type(l_type)==Unknown:
                for x in c:
                    if x.name==ast.lhs.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name, ArrayType(l.dimen, r_type)))
                        c.remove(x)
                l_type=r_type

            if type(r_type)==Unknown:
                for x in c:
                    if x.name==ast.rhs.name and type(x.mtype)==ArrayType:
                        c.append(Symbol(x.name,ArrayType(r.dimen, l_type)))
                        c.remove(x)
                r_type=l_type
            if type(l_type)!=type(r_type):
                raise TypeMismatchInStatement(ast)
    
    #Statement
    def visitIf(self,ast,c):
        for ifthen in ast.ifthenStmt:
            exp = self.visit(ifthen[0], c)

            if type(ifthen[0])==CallExpr:
                if type(exp.mtype.restype)==Unknown:
                    c.remove(exp)
                    c.append(Symbol(exp.name,MType(exp.mtype.intype,BoolType)))
                    exp=BoolType()
                elif type(exp.mtype.restype)==BoolType:
                    exp=BoolType()

                else:
                    raise TypeMismatchInExpression(ast)
            elif type(ifthen[0])==Id:
                if isinstance(exp.mtype,(Prim,Unknown)):
                    if type(exp.mtype)==Unknown:
                        c.remove(exp)
                        c.append(Symbol(exp.name,BoolType()))
                        exp=BoolType()
                    elif type(exp.mtype)==BoolType:
                        exp=BoolType()
                    else:
                        raise TypeMismatchInExpression(ast)
            elif type(ifthen[0])==ArrayCell:

                if type(exp.mtype.eletype)==Unknown:
                    c.remove(exp)
                    c.append(Symbol(exp.name,ArrayType(exp.mtype.dimen,BoolType)))
                    exp=BoolType()
                elif type(exp.mtype.eletype)==BoolType:
                    exp=BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            if type(exp)!=type(BoolType()):

                raise TypeMismatchInExpression(ast)
            local=reduce(lambda acc,ele:acc+[self.visit(ele,acc)],ifthen[1],[])
            name = [x.name for x in local]
            for x in c:
                if x.name not in name:
                    local += [x]

            # duyet statement
            for x in ifthen[2]:
                self.visit(x, local)

            # update global var
            for x in c:
                if x.name not in name:
                    for y in local:
                        if x.name == y.name and x!=y:
                            c.remove(x)
                            c.append(y)
        #else
        local = reduce(lambda acc, ele: acc + [self.visit(ele, acc)], ast.elseStmt[0], [])
        name = [x.name for x in local]
        for x in c:
            if x.name not in name:
                local += [x]

        # duyet statement
        for x in ast.elseStmt[1]:
            self.visit(x, local)

        # update global var
        for x in c:
            if x.name not in name:
                for y in local:
                    if x.name == y.name and x != y:
                        c.remove(x)
                        c.append(y)

    def visitFor(self,ast,c):
        exp1=self.visit(ast.expr1,c)
        exp2=self.visit(ast.expr2,c)
        exp3 = self.visit(ast.expr3, c)

        if type(ast.expr1)==Id:
            if type(exp1.mtype)==Unknown:
                c.remove(exp1)
                c.append(Symbol(exp1.name,IntType()))
                exp1=IntType()
            elif type(exp1.mtype)==IntType:
                exp1=IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif type(ast.expr1)==ArrayCell:
            if type(exp1.mtype.eletype)==Unknown:
                c.remove(exp1)
                c.append(Symbol(exp1.name,ArrayType(exp1.mtype.dimen,IntType())))
                exp1=IntType()
            elif type(exp1.mtype.eletype)==IntType:
                exp1=IntType()
            else:
                raise TypeMismatchInExpression(ast)

        if type(ast.expr2)==Id:
            if type(exp2.mtype) == Unknown:
                c.remove(exp2)
                c.append(Symbol(exp2.name, BoolType()))
                exp2 = BoolType()
            elif type(exp2.mtype) == BoolType:
                exp2 = BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif type(ast.expr2) == ArrayCell:
            if type(exp2.mtype.eletype) == Unknown:
                c.remove(exp2)
                c.append(Symbol(exp2.name, ArrayType(exp2.mtype.dimen, BoolType())))
                exp1 = BoolType()
            elif type(exp1.mtype.eletype)==BoolType:
                exp1 = BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        if type(ast.expr3)==Id:
            if type(exp3.mtype) == Unknown:
                c.remove(exp3)
                c.append(Symbol(exp3.name, IntType()))
                exp3 = IntType()
            elif type(exp3.mtype) == IntType:
                exp3 = IntType()
            else :
                raise TypeMismatchInExpression(ast)
        elif type(ast.expr1) == ArrayCell:
            if type(exp3.mtype.eletype) == Unknown:
                c.remove(exp3)
                c.append(Symbol(exp3.name, ArrayType(exp1.mtype.dimen, IntType())))
                exp3 = IntType()
            elif type(exp3.mtype.eletype)==IntType:
                exp3 = IntType()
            else:
                raise TypeMismatchInExpression(ast)

        if type(exp1)==IntType and type(exp3)==IntType and type(exp2)==BoolType:
            pass
        else:

            raise TypeMismatchInExpression(ast)
        local = reduce(lambda acc, ele: acc + [self.visit(ele, acc)], ast.loop[0], [])
        name = [x.name for x in local]
        for x in c:
            if x.name not in name:
                local += [x]

        # duyet statement
        for x in ast.loop[1]:
            self.visit(x, local)

        # update global var
        for x in c:
            if x.name not in name:
                for y in local:
                    if x.name == y.name and x != y:
                        c.remove(x)
                        c.append(y)

    def visitDowhile(self,ast,c):
        exp=self.visit(ast.exp,c)
        if type(exp)==type(BoolType()):
            pass
        else:
            raise TypeMismatchInExpression(ast)
        local = reduce(lambda acc, ele: acc + [self.visit(ele, acc)], ast.sl[0], [])
        name = [x.name for x in local]
        for x in c:
            if x.name not in name:
                local += [x]

        # duyet statement
        for x in ast.sl[1]:
            self.visit(x, local)

        # update global var
        for x in c:
            if x.name not in name:
                for y in local:
                    if x.name == y.name and x != y:
                        c.remove(x)
                        c.append(y)
    
    def visitWhile(self,ast,c):
        exp = self.visit(ast.exp, c)
        if type(exp) == type(BoolType()):
            pass
        else:
            raise TypeMismatchInExpression(ast)
        local = reduce(lambda acc, ele: acc + [self.visit(ele, acc)], ast.sl[0], [])
        name = [x.name for x in local]
        for x in c:
            if x.name not in name:
                local += [x]

        # duyet statement
        for x in ast.sl[1]:
            self.visit(x, local)

        # update global var
        for x in c:
            if x.name not in name:
                for y in local:
                    if x.name == y.name and x != y:
                        c.remove(x)
                        c.append(y)

    def visitReturn(self,ast,c):
        if ast.expr:
            return self.visit(ast.expr,c)
        return VoidType()
    
    def visitCallStmt(self,ast,c):
        f=0
        for x in c:
            if ast.method.name == x.name and type(x.mtype)==MType:
                f = x
        if f==0:
            raise Undeclared(Function(),ast.method.name)

        agru = [self.visit(x, c) for x in ast.param]
        if len(agru) != len(f.mtype.intype):
            raise TypeMismatchInStatement(ast)
        if "TypeCannotBeInferred" in agru:
            raise TypeCannotBeInferred(ast)

        if type(f.mtype.restype)!=Unknown:
            if type(f.mtype.restype)!=VoidType:
                raise TypeMismatchInStatement(ast)

            for i in range(len(agru)):
                if type(agru[i])==Unknown and type(f.mtype.intype[i])==Unknown:
                    raise TypeCannotBeInferred(ast)

                if type(agru[i])==ArrayType and type(f.mtype.intype[i])!=ArrayType:
                    raise TypeMismatchInStatement(ast)
                if type(agru[i])!=ArrayType and type(f.mtype.intype[i])==ArrayType:
                    raise TypeMismatchInStatement(ast)

                if type(agru[i])==Unknown:
                    if type(ast.param[i])==Id:
                        for x in c:
                            if x.name==ast.param[i].name and type(x.mtype)!=MType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)

                    if type(ast.param[i])==ArrayCell:
                        for x in c:
                            if x.name==ast.param[i].arr.name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,ArrayType(x.mtype.dimen,f.mtype.intype[i])))
                                c.remove(x)
                    agru[i]=f.mtype.intype[i]

                if type(agru[i])==Symbol:
                    c.append(Symbol(agru[i].name,MType(agru[i].mtype.intype,f.mtype.intype[i])))
                    agru[i] = f.mtype.intype[i]

                if type(f.mtype.intype[i])==Unknown:
                    f.mtype.intype[i]=agru[i]

                if type(agru[i])!=type(f.mtype.intype[i]):
                    raise TypeMismatchInStatement(ast)

                if type(agru[i] == ArrayType) and type(f.mtype.intype[i]) == ArrayType:
                    if f.mtype.intype[i].dimen != agru[i].dimen:
                        raise TypeMismatchInExpression(ast)
                    if type(f.mtype.intype[i].eletype) == Unknown and type(agru[i].eletype) == Unknown:
                        return TypeCannotBeInferred(ast)
                    if type(f.mtype.intype[i].eletype) == Unknown:
                        f.mtype.intype[i].eletype = agru[i].eletype
                    if type(agru[i].eletype) == Unknown:
                        for x in c:
                            if x.name == ast.param[i].name and type(x.mtype) == ArrayType:
                                c.append(Symbol(x.name, f.mtype.intype[i]))
                                c.remove(x)
                        agru[i] = f.mtype.intype[i]
                    if type(f.mtype.intype[i].eletype) != type(agru[i].eletype):
                        raise TypeMismatchInExpression(ast)

        #Inference type of function
        if type(f.mtype.restype)==Unknown:
            for x in agru:
                if type(x)==Unknown or type(x)==Symbol:
                    raise TypeCannotBeInferred(ast)

            for x in c:
                if x.name==ast.method.name and type(x.mtype)==MType:
                    c.remove(x)
            newfunc=Symbol(ast.method.name,MType(agru,VoidType()))
            c.append(newfunc)

    def visitBreak(self,ast,c):
        pass

    def visitContinue(self,ast,c):
        pass
    #Id
    def visitId(self,ast,c):
        for x in c:
            if ast.name==x.name and type(x.mtype)!=MType:
                return x.mtype
        raise Undeclared(Identifier(),ast.name)

    #ArrayCell
    def visitArrayCell(self,ast,c):
        arr=self.visit(ast.arr,c)
        if arr=="TypeCannotBeInferred":
            return "TypeCannotBeInferred"
        if not isinstance(arr,ArrayType):
            raise TypeMismatchInExpression(ast)

        listexpr=[self.visit(x,c) for x in ast.idx]
        if "TypeCannotBeInferred" in listexpr:
            return "TypeCannotBeInferred"

        for i in range(len(listexpr)):
            if type(listexpr[i])==Unknown:
                if type(ast.idx[i])==Id:
                    for x in c:
                        if x.name==ast.idx[i].name:
                            x.mtype=IntType()
                if type(ast.idx[i])==ArrayCell:
                    for x in c:
                        if x.name==ast.idx[i].arr.name and type(x.mtype)==ArrayType:
                            x.mtype.eletype=IntType()
                listexpr[i]=IntType()
            if type(listexpr[i])==Symbol:
                c.append(Symbol(listexpr[i].name,MType(listexpr[i].mtype.intype,IntType())))
                listexpr[i]=IntType()

        if len(arr.dimen)!=len(listexpr):
            raise TypeMismatchInExpression(ast)
        for x in listexpr:
            if not isinstance(x,IntType):
                raise TypeMismatchInExpression(ast)
        return arr.eletype

    #Exp
    def visitBinaryOp(self,ast,o):
        l = self.visit(ast.left, o)
        r = self.visit(ast.right, o)
        if l==-1 or r==-1:
            return -1
        if l==-2 or r==-2:
            return -2
        ltype=l
        rtype=r

        if ast.left.__class__.__name__=='Id':
            if type(l.mtype) == type(ArrayType(None, None)):
                raise TypeMismatchInExpression(ast)
            else:
                ltype=l.mtype
        if ast.right.__class__.__name__=='Id':

            if type(r.mtype) == type(ArrayType(None, None)):
                raise TypeMismatchInExpression(ast)
            else:
                rtype=r.mtype

        if ast.op in ['==','!=','<','>','<=','>=','+','-','*','\\','%']:
            if type(ltype)==type(Unknown()) :
                ltype=IntType()
            if type(rtype)==type(Unknown()):
                rtype=IntType()
            if type(ltype) != type(IntType()) or type(rtype)!=type(IntType()):
                raise TypeMismatchInExpression(ast)
            #if ctx.op in ['==','!=','<','>','<=','>=']:
            #    return BoolType()
           # else:
             #   return IntType()
        else:
            if type(ltype)==type(Unknown()) :
                ltype=FloatType()
            if type(rtype)==type(Unknown()):
                rtype=FloatType()
            if type(ltype) != type(FloatType()) or type(rtype)!=type(FloatType()):
                raise TypeMismatchInExpression(ast)
           ##   return BoolType()
          #  else:
             #   return FloatType()

        if ast.left.__class__.__name__ == 'Id':
            o.remove(l)
            o.append(Symbol(l.name, ltype))

        if ast.right.__class__.__name__ == 'Id':
            o.remove(r)
            o.append(Symbol(r.name, rtype))

        if ast.op in ['==','!=','<','>','<=','>=','==','!=','<','>','<=','>=']:
            return BoolType()
        elif ast.op in ['+','-','*','\\','%']:


            return IntType()
        else:
            return FloatType()

    def visitUnaryOp(self,ast,o):
        exp=self.visit(ast.body,o)
        etype=exp
        if type(ast.body)==CallExpr:
            for i in o:
                if i.name == ast.body.method.name:

                    etype=i.mtype.restype

        if ast.body.__class__.__name__ == 'Id':
            if type(exp.mtype) == type(ArrayType(None, None)):
                raise TypeMismatchInExpression(ast)
            else:
                etype = exp.mtype

        if ast.op in ['-']:
            if type(etype)==type(Unknown()) :
                etype=IntType()
            if type(etype) !=type(IntType()):
                raise TypeMismatchInExpression(ast)
        if ast.op =='-.':
            if type(etype)==type(Unknown()) :
                etype=FloatType()
            if type(etype) !=type(FloatType()):
                raise TypeMismatchInExpression(ast)
        if ast.op == ['!']:
            if type(etype)==type(Unknown()) :
                etype=BoolType()
            if type(etype) !=type(BoolType()):
                raise TypeMismatchInExpression(ast)

        if ast.body.__class__.__name__ == 'Id':
                o.remove(exp)
                o.append(Symbol(exp.name, etype))
        return etype

    

    def visitCallExpr(self,ast,c):
        f=0
        for x in c:
            if ast.method.name==x.name and type(x.mtype)==MType:
                f=x
        if f==0:
            raise Undeclared(Function(),ast.method.name)

        agru=[self.visit(x,c) for x in ast.param]

        if len(agru) != len(f.mtype.intype):
            raise TypeMismatchInExpression(ast)
        if "TypeCannotBeInferred" in agru:
            return "TypeCannotBeInferred"
        if type(f.mtype.restype)!=Unknown:
            for i in range(len(agru)):
                if type(agru[i])==Unknown and type(f.mtype.intype[i])==Unknown:
                    return "TypeCannotBeInferred"
                if type(agru[i])==ArrayType and type(f.mtype.intype[i])!=ArrayType:
                    raise TypeMismatchInExpression(ast)
                if type(agru[i])!=ArrayType and type(f.mtype.intype[i])==ArrayType:
                    raise TypeMismatchInExpression(ast)

                if type(agru[i])==Unknown:
                    if type(ast.param[i])==Id:
                        for x in c:
                            if x.name==ast.param[i].name and type(x.mtype)!=MType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)

                    if type(ast.param[i])==ArrayCell:
                        for x in c:
                            if x.name==ast.param[i].arr.name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,ArrayType(x.mtype.dimen,f.mtype.intype[i])))
                                c.remove(x)
                    agru[i]=f.mtype.intype[i]

                if type(agru[i])==Symbol:
                    c.append(Symbol(agru[i].name,MType(agru[i].mtype.intype,f.mtype.intype[i])))
                    agru[i] = f.mtype.intype[i]

                if type(f.mtype.intype[i])==Unknown:
                    f.mtype.intype[i]=agru[i]

                if type(agru[i])!=type(f.mtype.intype[i]):
                    raise TypeMismatchInExpression(ast)

                if type(agru[i]==ArrayType) and type(f.mtype.intype[i])==ArrayType:
                    if f.mtype.intype[i].dimen!=agru[i].dimen:
                        raise TypeMismatchInExpression(ast)
                    if type(f.mtype.intype[i].eletype)==Unknown and type(agru[i].eletype)==Unknown:
                        return "TypeCannotBeInferred"
                    if type(f.mtype.intype[i].eletype) == Unknown:
                        f.mtype.intype[i].eletype=agru[i].eletype
                    if type(agru[i].eletype)==Unknown:
                        for x in c:
                            if x.name==ast.param[i].name and type(x.mtype)==ArrayType:
                                c.append(Symbol(x.name,f.mtype.intype[i]))
                                c.remove(x)
                        agru[i]=f.mtype.intype[i]
                    if type(f.mtype.intype[i].eletype)!=type(agru[i].eletype):
                        raise TypeMismatchInExpression(ast)

            return f.mtype.restype

        if type(f.mtype.restype) == Unknown:
            for x in agru:
                if type(x)==Unknown:
                    return "TypeCannotBeInferred"

            for x in c:
                if x.name==ast.method.name and type(x.mtype)==MType:
                    c.remove(x)
            newfunc=Symbol(ast.method.name,MType(agru,Unknown()))
            return newfunc

    #Literal
    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitArrayLiteral(self, ast, c):
        dimen = [len(ast.value)]
        ele = ast.value[0]
        while type(ele) == ArrayLiteral:
            dimen.append(len(ele.value))
            ele = ele.value[0]
        return ArrayType(dimen, self.visit(ele, None))

    



