#Cau1
    def visitVarDecl(self,ctx,o):
        ##if type(ctx.varType) is ArrayType: raise Exception("Array type variable found")
        self.emit.printout(self.emit.emitATTRIBUTE(ctx.variable.name, ctx.varType, True, 5))
        return Symbol(ctx.variable.name, ctx.varType, CName(self.className))

    def visitVarDecl(self,ctx,o):
        _env = o.sym if type(o) is SubBody else []
        _frame = o.frame
        _idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(_idx, ctx.variable.name, ctx.varType, _frame.getStartLabel(), _frame.getEndLabel(), _frame))
        return SubBody(_frame, [Symbol(ctx.variable.name, ctx.varType, Index(_idx))] + _env) 
        
  