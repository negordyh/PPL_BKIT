from functools import reduce
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardec = ctx.vardecl()
        return Program(list(reduce(lambda a,b: a + self.visit(b), vardec,[])))

    def visitVardecl(self,ctx:MPParser.VardeclContext):
        type = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x, type), ids))

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if(ctx.INTTYPE()) else FloatType()
        
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]