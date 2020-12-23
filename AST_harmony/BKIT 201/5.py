from functools import reduce
class ASTGeneration(MPVisitor):

   # program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardec = ctx.vardecl()
        return Program(list(reduce(lambda a,b: a + self.visit(b), vardec,[])))

    #vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        type = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x, type), ids))

    #mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if(ctx.INTTYPE()) else FloatType()
        
    #ids: ID (',' ID)*; 
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(x.getText()) for x in ctx.ID()]
