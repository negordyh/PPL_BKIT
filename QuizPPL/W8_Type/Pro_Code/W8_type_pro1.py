

class StaticCheck(Visitor):

    def visitBinOp(self, ctx: BinOp, o): 
        ltype = self.visit(ctx.e1, o)
        rtype = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-', '*']:
            if type(ltype) is BoolType or type(rtype) is BoolType:
                raise TypeMismatchInExpression(ctx)
            elif type(ltype) is FloatType or type(rtype) is FloatType:
                return FloatType()
            else: 
                return IntType()

        elif ctx.op in ['/']:
            if type(ltype) is BoolType or type(rtype) is BoolType:
                raise TypeMismatchInExpression(ctx)
            else: return FloatType()
            
        elif ctx.op in ['&&', '||']:
            if type(ltype) is BoolType or type(rtype) is BoolType:
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)

        else:
            if type(ltype) == type(rtype):
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)

    def visitUnOp(self, ctx: UnOp, o): 
        itype = self.visit(ctx.e, o[:])
        if ctx.op in ['-']:
            if type(itype) is FloatType:
                return FloatType()
            if type(itype) is IntType:
                return IntType
            else: raise TypeMismatchInExpression(ctx)
        if ctx.op in ['!']:
            if type(itype) is BoolType:
                return BoolType()
            else: raise TypeMismatchInExpression(ctx)

    def visitIntLit(self, ctx: IntLit,o): 
        return IntType()
    def visitFloatLit(self, ctx: FloatLit, o): 
        return FloatType()
    def visitBoolLit(self, ctx: BoolLit, o): 
        return BoolType()

