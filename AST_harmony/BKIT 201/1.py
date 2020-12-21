class ASTGeneration(MPVisitor):
# INTTYPE: 'int';
# FLOATTYPE: 'float';
# ID: [a-z]+ ;
    # program: vardecls EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    # vardecls: vardecl vardecltail;
    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.vardecltail() else 0

    # vardecl: mptype ids ';' ;
    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1
        
    # ids: ID ',' ids | ID;
    def visitIds(self, ctx: MPParser.IdsContext):
        return 2 + self.visit(ctx.ids()) if(ctx.ids()) else 1
