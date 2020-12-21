    def visitAssign(self,ctx,o):     
        rightCode, typeRight = self.visit(ctx.rhs, Access(o.frame, o.sym, False, True))
        leftCode, typeLeft = self.visit(ctx.lhs, Access(o.frame, o.sym, True, False))
        self.emit.printout(rightCode + leftCode)