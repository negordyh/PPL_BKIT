class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        le = self.visit(ctx.e1, o)
        re = self.visit(ctx.e2, o)
        if(ctx.op in ['+','-','*']):
            if(le == 'bool' or re == 'bool'):
                raise TypeMismatchInExpression(ctx)
            elif(le == 'float' or re == 'float'):
                return 'float'
            else: return 'int'
        elif(ctx.op == '/'):
            if(le == 'bool' or re == 'bool'):
                raise TypeMismatchInExpression(ctx)
            else: return 'float'
        elif(ctx.op in ['&&', '||']):
            if(le == 'bool' and re == 'bool'):
                return 'bool'
            else: raise TypeMismatchInExpression(ctx)
        else: 
            if(le == re):  
                return 'bool'     
            else: raise TypeMismatchInExpression(ctx)     

    def visitUnOp(self,ctx:UnOp,o):
        ex = self.visit(ctx.e, o)
        if(ctx.op == '!'):
            if(ex == 'bool'):
                return 'bool'
            else: raise TypeMismatchInExpression(ctx)
        if(ctx.op == '-'):
                if(ex == 'float'):
                    return 'float'
                if(ex == 'int'):
                    return 'int'
                else: raise TypeMismatchInExpression(ctx)
            
    def visitIntLit(self,ctx:IntLit,o):
        return 'int'
    def visitFloatLit(self,ctx,o):
        return 'float'
    def visitBoolLit(self,ctx,o):
        return 'bool'