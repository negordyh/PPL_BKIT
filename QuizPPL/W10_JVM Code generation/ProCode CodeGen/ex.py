def visitBinExpr(self, ctx, o):
        lC, lT = self.visit(ctx.e1, o)
        rC, rT = self.visit(ctx.e2, o)
        if ctx.op in ['+', '-']:
            return lC + rC + self.emit.emitADDOP(ctx.op, IntType(), o.frame), IntType()
        elif ctx.op in ['*', '/']:
            return lC + rC + self.emit.emitMULOP(ctx.op, IntType(), o.frame), IntType()
        elif ctx.op in ['+.', '-.']:
            return lC + rC + self.emit.emitADDOP(ctx.op[:-1], FloatType(), o.frame), FloatType()
        else:
            return lC + rC + self.emit.emitMULOP(ctx.op[:-1], FloatType(), o.frame), FloatType()