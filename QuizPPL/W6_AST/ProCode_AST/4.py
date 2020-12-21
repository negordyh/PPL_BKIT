class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

# exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MPParser.ExpContext):
        return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp())) if ctx.ASSIGN() else self.visit(ctx.term())

#term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext):
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1))) if ctx.COMPARE() else self.visit(ctx.factor(0))

# factor: factor ANDOR operand | operand;
    def visitFactor(self,ctx:MPParser.FactorContext):
        return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand())) if ctx.ANDOR() else self.visit(ctx.operand())
        
# operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        return self.visit(ctx.exp()) if ctx.getChildCount() == 3 else IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else BooleanLiteral(ctx.BOOLIT().getText()) if ctx.BOOLIT() else Id(ctx.ID().getText())