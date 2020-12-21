    def visitFuncDecl(self, ctx, o):
        glo_env = o.sym
        retType = ctx.returnType if ctx.returnType else VoidType()
        frame = Frame(ctx.name, retType)
        inType = [x.typ for x in ctx.param]
        mType = MType(inType, retType)
        self.emit.printout(self.emit.emitMETHOD(ctx.name, mType, True))
        frame.enterScope(type(retType) == VoidType)
        inType = []
        mType = MType(inType, retType)
        sub = SubBody(frame, glo_env)
        [self.visit(x, sub) for x in ctx.param]
        [self.visit(x, sub) for x in ctx.body[0]]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        [self.visit(x, sub) for x in ctx.body[1]]
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return Symbol(ctx.name, mType, CName(self.className ))