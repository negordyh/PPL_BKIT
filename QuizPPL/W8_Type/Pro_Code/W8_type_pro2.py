from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)], acc[1] + [self.visit(ele, acc)]], ctx.decl, [[], []])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name, o[0])):
            raise RedeclaredVariable(ctx.name)
        return ctx

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name, o[0])):
            raise RedeclaredConstant(ctx.name)
        return ctx
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if list(filter(lambda x: x.name == ctx.name, o[0])):
            raise RedeclaredFunction(ctx.name)
        o[1].append(ctx)
        check = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)], acc[1] + [self.visit(ele, acc)]], ctx.param + ctx.body[0], [[], o[1]])
        for x in ctx.body[1]:
            self.visit(x, check[1]) 
        return ctx

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        if list(filter(lambda x: x.name == ctx.name, o)): pass
        else:
            raise UndeclaredIdentifier(ctx.name)


class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = {}
        for x in ctx.decl:
            self.visit(x, o)
        self.visit(ctx.exp, o)

    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name] = ctx.typ

    def visitBinOp(self, ctx: BinOp, o): 
        l = self.visit(ctx.e1, o)
        r = self.visit(ctx.e2, o)
        if (ctx.op in ['+', '-', '*']):
            if (type(l) is BoolType or type(r) is BoolType):
                raise TypeMismatchInExpression(ctx)
            elif (type(l) is FloatType or type(r) is FloatType):
                return FloatType()
            else: return IntType()

        elif (ctx.op == '/'):
            if (type(l) is BoolType or type(r) is BoolType):
                raise TypeMismatchInExpression(ctx)
            else: return FloatType()
            
        elif (ctx.op in ['&&', '||']):
            if (type(l) is BoolType and type(r) is BoolType):
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)

        else:
            if (type(l) == type(r)):
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o): 
        ex = self.visit(ctx.e, o)
        if (ctx.op == '!'):
            if (type(itype) == BoolType):
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)
        if (ctx.op == '-'):
            if (type(ex) == FloatType):
                return FloatType()
            if (type(ex) == IntType):
                return IntType()
            else: raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit,o): 
        return IntType()
    def visitFloatLit(self, ctx: FloatLit, o): 
        return FloatType()
    def visitBoolLit(self, ctx: BoolLit, o): 
        return BoolType()

    def visitId(self,ctx,o):
        if(ctx.name in o.keys()):
            return o[ctx.name]
        else: raise UndeclaredIdentifier(ctx.name)