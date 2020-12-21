    def visitVarDecl(self,ctx,o):
        isLocal = o.frame
        if isLocal:
            index = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ctx.name, ctx.typ, isLocal.getStartLabel(), isLocal.getEndLabel()))
            return Symbol(ctx.name, ctx.typ, Index(index))
        else:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False))
            return Symbol(ctx.name, ctx.typ, CName(self.className))