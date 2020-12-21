    
    
    #Cau1
    def visitIntLiteral(self,ctx,o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ctx.value, frame), IntType()

    #Cau2
    def visitFloatLiteral(self, ctx, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ctx.value), frame), FloatType()


    #Cau3
    def visitBinExpr(self,ctx,o):
        ctxt = o
        frame = ctxt.frame
        left, typeLeft = self.visit(ctx.e1, o)
        right, typeRight = self.visit(ctx.e2, o)
        if not(type(typeLeft) == type(typeRight)):
            if type(typeLeft) is IntType and type(typeRight) is FloatType:
                left += self.emit.emitI2F(frame)
                typeLeft = FloatType()
            elif type(typeLeft) is FloatType and type(typeRight) is IntType:
                right += self.emit.emitI2F(frame)
                typeRight = FloatType()
        if ctx.op in ['+','-']: return left + right + self.emit.emitADDOP(ctx.op, typeLeft, frame), typeLeft
        elif ctx.op in ['*', '/']: return left + right + self.emit.emitMULOP(ctx.op, typeLeft, frame), typeLeft
        elif ctx.op in ['+.', '-.']: return left + right + self.emit.emitADDOP(ctx.op[:-1], typeLeft, frame), typeLeft
        else:
            return left + right + self.emit.emitMULOP(ctx.op[:-1], typeLeft, frame), typeLeft

    #Cau4
    def visitBinExpr(self,ctx,o):
        ctxt = o
        frame = ctxt.frame
        left, typeLeft = self.visit(ctx.e1, o)
        right, typeRight = self.visit(ctx.e2, o)
        if not(type(typeLeft) == type(typeRight)):
            if type(typeLeft) is IntType and type(typeRight) is FloatType:
                left += self.emit.emitI2F(frame)
                typeLeft = FloatType()
            elif type(typeLeft) is FloatType and type(typeRight) is IntType:
                right += self.emit.emitI2F(frame)
                typeRight = FloatType()
        if ctx.op in ['+','-']: return left + right + self.emit.emitADDOP(ctx.op, typeLeft, frame), typeLeft
        elif ctx.op == '*': return left + right + self.emit.emitMULOP(ctx.op, typeLeft, frame), typeLeft
        elif ctx.op == '/':
            if type(typeLeft) is IntType: return left + self.emit.emitI2F(frame) + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(ctx.op, FloatType(), frame), FloatType()
            else: return left + right + self.emit.emitMULOP(ctx.op, typeLeft, frame), typeLeft
        elif ctx.op in ['>','<','>=','<=','!=','==']: return left + right + self.emit.emitREOP(ctx.op, typeLeft, frame), BoolType()


    #Cau5
    def visitId(self, ctx, o):
        sym = self.lookup(ctx.name.lower(), o.sym, lambda x:x.name.lower())
        if not sym: raise Undeclared(Variable(), ctx.name)
        if o.isLeft:
            if type(sym.value) is CName: return self.emit.emitPUTSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype
            else: return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName: return self.emit.emitGETSTATIC(sym.value.value + '/' + sym.name, sym.mtype, o.frame), sym.mtype
            else: return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
      
        
        
      