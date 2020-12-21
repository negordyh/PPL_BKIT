from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        o=reduce(lambda a,b: a+[self.visit(b,a)],ctx.decl,[])
        [self.visit(x,o) for x in ctx.stmts]

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
        r=self.visit(ctx.rhs,o)
        l=self.visit(ctx.lhs,o)
        
        if l=="":
            l=r
            for x in o:
                if x==(ctx.lhs.name,""):
                    o.remove(x)
                    o.append((ctx.lhs.name,r))
                    
        if l!="" and r=="":
            r=l
            for x in o:
                if x==(ctx.rhs.name,""):
                    o.remove(x)
                    o.append((ctx.rhs.name,r))
        if r=="":
            raise TypeCannotBeInferred(ctx)
        if l!=r:
            raise TypeMismatchInStatement(ctx)
      
    def visitBinOp(self,ctx:BinOp,o):
        l=self.visit(ctx.e1,o)
        if l=="":
            for x in o:
                if x==(ctx.e1.name,""):
                    o.remove(x)
                    if ctx.op in ["+","-","*","/",">","="]:
                        o.append((ctx.e1.name,"int"))
                        l="int"
                    if ctx.op in ["+.","-.","*.","/.",">.","=."]:
                        o.append((ctx.e1.name,"float"))
                        l="float"
                    if ctx.op in ["&&", "||", ">b", "=b"]:
                        o.append((ctx.e1.name,"bool"))
                        l="bool"
        
        r=self.visit(ctx.e2,o)
        if r=="":
            for x in o:
                if x==(ctx.e2.name,""):
                    o.remove(x)
                    if ctx.op in ["+","-","*","/",">","="]:
                        o.append((ctx.e2.name,"int"))
                        r="int"
                    if ctx.op in ["+.","-.","*.","/.",">.","=."]:
                        o.append((ctx.e2.name,"float"))
                        r="float"
                    if ctx.op in ["&&", "||", ">b", "=b"]:
                        o.append((ctx.e2.name,"bool"))
                        r="bool"

        if ctx.op in ["+","-","*","/",">","="]:
            if l!="int" or r!="int":
                raise TypeMismatchInExpression(ctx)
            if ctx.op in [">","="]:
                return "bool"
            return "int"
        
        if ctx.op in ["+.","-.","*.","/.",">.","=."]:
            if l!="float" or r!="float":
                raise TypeMismatchInExpression(ctx)
            if ctx.op in [">.","=."]:
                return "bool"
            return "float"
        
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if l!="bool" or r!="bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"  

    def visitUnOp(self,ctx:UnOp,o):
        r=self.visit(ctx.e,o)
        if r=="":
            for x in o:
                if x==(ctx.e.name,""):
                    o.remove(x)
                    if ctx.op in ["-","i2f"]:
                        o.append((ctx.e.name,"int"))
                        r="int"
                    if ctx.op in ["-.","floor"]:
                        o.append((ctx.e.name,"float"))
                        r="float"
                    if ctx.op =="!":
                        o.append((ctx.e.name,"bool"))
                        r="bool"

        if ctx.op in ["-","i2f"]:
            if r!="int":
                raise TypeMismatchInExpression(ctx)
            if ctx.op == "i2f":
                return "float"
            return "int"
        
        if ctx.op in ["-.","floor"]:
            if r!="float":
                raise TypeMismatchInExpression(ctx)
            if ctx.op == "floor":
                return "int"
            return "float"
            
        if r!="bool":
            raise TypeMismatchInExpression(ctx)
        return "bool"

    def visitIntLit(self,ctx:IntLit,o):
        return "int"

    def visitFloatLit(self,ctx,o):
        return "float"

    def visitBoolLit(self,ctx,o):
        return "bool"

    def visitId(self,ctx,o):
        for x in o:
            if ctx.name in x[0]:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)