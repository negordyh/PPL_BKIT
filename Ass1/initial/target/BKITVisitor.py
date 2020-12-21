# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr_decl.
    def visitArr_decl(self, ctx:BKITParser.Arr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexes.
    def visitIndexes(self, ctx:BKITParser.IndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index.
    def visitIndex(self, ctx:BKITParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter.
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idlist.
    def visitIdlist(self, ctx:BKITParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arraytype.
    def visitArraytype(self, ctx:BKITParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt1.
    def visitStmt1(self, ctx:BKITParser.Stmt1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt2.
    def visitStmt2(self, ctx:BKITParser.Stmt2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl_stmt.
    def visitVar_decl_stmt(self, ctx:BKITParser.Var_decl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:BKITParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela_operator.
    def visitRela_operator(self, ctx:BKITParser.Rela_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#add.
    def visitAdd(self, ctx:BKITParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sub.
    def visitSub(self, ctx:BKITParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mul.
    def visitMul(self, ctx:BKITParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#div.
    def visitDiv(self, ctx:BKITParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lit.
    def visitLit(self, ctx:BKITParser.LitContext):
        return self.visitChildren(ctx)



del BKITParser