    def visitIf(self, ast, o):
        ctxt = o
        frame = o.frame
        expCode, expType = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
        labelF = frame.getNewLabel()
        labelT = frame.getNewLabel() if ast.estmt else None
        self.emit.printout(expCode  + self.emit.emitIFFALSE(labelF, frame))
        thenStmt = self.visit(ast.tstmt , ctxt)
        self.emit.printout(self.emit.emitGOTO(labelT,frame)) if ast.estmt else None
        self.emit.printout(self.emit.emitLABEL(labelF, frame))

        elseStmt = None
        if ast.estmt:
            elseStmt = self.visit(ast.estmt , ctxt)
            self.emit.printout(self.emit.emitLABEL(labelT, frame))