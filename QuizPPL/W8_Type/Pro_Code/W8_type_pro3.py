#TypeCannotBeInferred : khong suy dien duoc
#TypeMismatchInStatement
#TypeMismatchInExpression


class IntType(ABC):
    pass
class FloatType(ABC):
    pass
class BoolType(ABC):
    pass
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [[x.name, None] for x in ctx.decl]
        [self.visit(x, o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitAssign(self,ctx:Assign,o):
        right = self.visit(ctx.rhs, o)
        left = self.visit(ctx.lhs, o)
        if not left and not right:
            raise TypeCannotBeInferred(ctx)
        if not left:
            for x in o:
                if ctx.lhs.name == x[0]:
                    x[1] = right
                    return;
        if not right:
            for x in o:
                if ctx.rhs.name == x[0]:
                    x[1] = left
                    return;
        if type(left) != type(right):
            raise TypeMismatchInStatement(ctx)
        

    def visitBinOp(self,ctx:BinOp,o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        if ctx.op in ['+','-','*','/']:
            if not left:
                left = IntType()
                for x in o:
                    if ctx.e1.name == x[0]:
                        x[1] = IntType()
            if not right:
                right = IntType()
                for x in o:
                    if ctx.e2.name == x[0]:
                        x[1] = IntType()
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

        if ctx.op in ['+.','-.','*.','/.']:
            if not left:
                left = FloatType()
                for x in o:
                    if ctx.e1.name == x[0]:
                        x[1] = FloatType()
            if not right:
                right = FloatType()
                for x in o:
                    if ctx.e2.name == x[0]:
                        x[1] = FloatType()
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()

        if ctx.op in ['>', '=']:
            if not left:
                left = IntType()
                for x in o:
                    if ctx.e1.name == x[0]:
                        x[1] = IntType()
            if not right:
                right = IntType()
                for x in o:
                    if ctx.e2.name == x[0]:
                        x[1] = IntType()
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        if ctx.op in ['>.', '=.']:
            if not left:
                left = FloatType()
                for x in o:
                    if ctx.e1.name == x[0]:
                        x[1] = FloatType()
            if not right:
                right = FloatType()
                for x in o:
                    if ctx.e2.name == x[0]:
                        x[1] = FloatType()
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        if ctx.op in ['&&', '||', '>b', '=b']:
            if not left:
                left = BoolType()
                for x in o:
                    if ctx.e1.name == x[0]:
                        x[1] = BoolType()
            if not right:
                right = BoolType()
                for x in o:
                    if ctx.e2.name == x[0]:
                        x[1] = BoolType()
            if type(left) != BoolType or type(right) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op == '-':
            if not e:
                e = IntType()
                for x in o:
                    if ctx.e.name == x[0]:
                        x[1] = IntType()
            if type(e) != IntType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

        if ctx.op == '-.':
            if not e:
                e = FloatType()
                for x in o:
                    if ctx.e.name == x[0]:
                        x[1] = FloatType()
            if type(e) != FloatType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        
        if ctx.op == '!':
            if not e:
                e = BoolType()
                for x in o:
                    if ctx.e.name == x[0]:
                        x[1] = BoolType()
            if type(e) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        if ctx.op == 'i2f':
            if not e:
                e = IntType()
                for x in o:
                    if ctx.e.name == x[0]:
                        x[1] = IntType()
            if type(e) != IntType:
                raise TypeMismatchInExpression(ctx)
            return FloatType()

        if ctx.op == 'floor':
            if not e:
                e = FloatType()
                for x in o:
                    if ctx.e.name == x[0]:
                        x[1] = FloatType()
            if type(e) != FloatType:
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self,ctx,o):
        for x in o:
            if ctx.name == x[0]:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)