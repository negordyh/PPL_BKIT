    def visitWhile(self, ast, o):
        ctxt = o
        frame = o.frame
        sym = o.sym
        frame.enterLoop()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        expCode, expType = self.visit(ast.expr, Access(frame, sym, False, True))
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame) + expCode + self.emit.emitIFFALSE(labelBreak, frame))
        self.visit(ast.stmt , ctxt)
        self.emit.printout(self.emit.emitGOTO(labelContinue,frame) + self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()