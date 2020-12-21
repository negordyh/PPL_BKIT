from functools import reduce
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

# exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        rl = ctx.term()[::-1]
        cl = zip(ctx.ASSIGN()[::-1], rl[1:])
        dl = zip(ctx.ASSIGN(), ctx.term()[1:])
        return reduce(lambda x,y:Binary(y[0].getText(),self.visit(y[1]), x),cl,self.visit(rl[0]))

#term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext):
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else self.visit(ctx.factor(0))

# factor: operand (ANDOR operand)*;
    def visitFactor(self,ctx:MPParser.FactorContext):
        rl = ctx.operand()[::-1]
        cl = zip(ctx.ANDOR()[::-1],rl[1:])
        dl = zip(ctx.ANDOR(), ctx.operand()[1:])
        return reduce(lambda x,y:Binary(y[0].getText(), x, self.visit(y[1])),dl,self.visit(ctx.operand()[0]))
        
# operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        return self.visit(ctx.exp()) if ctx.getChildCount() == 3 else IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else BooleanLiteral(ctx.BOOLIT().getText()) if ctx.BOOLIT() else Id(ctx.ID().getText())