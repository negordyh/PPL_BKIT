class ASTGeneration(MPVisitor):
# program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(self.visit(ctx.vardecls()))

# vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

# vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if(ctx.vardecltail()) else []

# vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext):
        type = self.visit(ctx.mptype())
        ids = self.visit(ctx.ids())
        return list(map(lambda x: VarDecl(x, type), ids))

# mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):
        return IntType() if(ctx.INTTYPE()) else FloatType()
        
# ids: ID ',' ids | ID;,
    def visitIds(self,ctx:MPParser.IdsContext):
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids()) if(ctx.getChildCount() == 3) else [Id(ctx.ID().getText())]