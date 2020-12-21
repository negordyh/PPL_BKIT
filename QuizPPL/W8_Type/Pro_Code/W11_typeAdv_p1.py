from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o = [[x.name, None] for x in ctx.decl]
        [self.visit(x, o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): 
        for x in o:
            if ctx.name==x[0]:
                raise Redeclared(ctx)
        return (ctx.name,"")

    def visitBlock(self,ctx:Block,o):
        
        block=reduce(lambda a,b: a+[self.visit(b,a)],ctx.decl,[])
        
        a=[x[0] for x in block]
        for x in o:
            if x[0] in a:
                pass
            else:
                block.append(x)
                    
            
        for stmt in ctx.stmts:
            self.visit(stmt,block)
        
        ctxname=[x.name for x in ctx.decl]    
        for x in o:
            if x[0] not in ctxname:
                for y in block:
                    if x[0]==y[0]:
                        o.remove(x)
                        o.append(y)

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

        if left=="":
            for x in o:
                if x==(ctx.e1.name,""):
                    o.remove(x)
                    if ctx.op in ["+","-","*","/",">","="]:
                        o.append((ctx.e1.name,IntType))
                        left=IntType
                    if ctx.op in ["+.","-.","*.","/.",">.","=."]:
                        o.append((ctx.e1.name,FloatType))
                        left=FloatType
                    if ctx.op in ["&&", "||", ">b", "=b"]:
                        o.append((ctx.e1.name,BoolType))
                        left=BoolType

        if right=="":
            for x in o:
                if x==(ctx.e2.name,""):
                    o.remove(x)
                    if ctx.op in ["+","-","*","/",">","="]:
                        o.append((ctx.e2.name,IntType))
                        right=IntType
                    if ctx.op in ["+.","-.","*.","/.",">.","=."]:
                        o.append((ctx.e2.name,FloatType))
                        right=FloatType
                    if ctx.op in ["&&", "||", ">b", "=b"]:
                        o.append((ctx.e2.name,BoolType))
                        right=BoolType

        if ctx.op in ["+","-","*","/",">","="]:
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ctx)
            if ctx.op in [">","="]:
                return BoolType()
            return IntType()

        if ctx.op in ["+.","-.","*.","/.",">.","=."]:
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ctx)
            if ctx.op in [">.","=."]:
                return BoolType()
            return FloatType()

        if ctx.op in ['&&', '||', '>b', '=b']:
            if type(left) != BoolType or type(right) != BoolType:
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self,ctx:UnOp,o):
        r=self.visit(ctx.e,o)
        if r=="":
            for x in o:
                if x==(ctx.e.name,""):
                    o.remove(x)
                    if ctx.op in ["-","i2f"]:
                        o.append((ctx.e.name,IntType))
                        r=IntType
                    if ctx.op in ["-.","floor"]:
                        o.append((ctx.e.name,FloatType))
                        r=FloatType
                    if ctx.op =="!":
                        o.append((ctx.e.name,BoolType))
                        r=BoolType

        if ctx.op in ["-","i2f"]:
            if type(r) != IntType:
                raise TypeMismatchInExpression(ctx)
            if ctx.op == "i2f":
                return FloatType()
            return IntType()
        
        if ctx.op in ["-.","floor"]:
            if r!=FloatType:
                raise TypeMismatchInExpression(ctx)
            if ctx.op == "floor":
                return IntType()
            return FloatType()
            
        if r!=BoolType:
            raise TypeMismatchInExpression(ctx)
        return BoolType()

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