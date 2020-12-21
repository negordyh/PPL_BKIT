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


    # Visit a parse tree produced by BKITParser#varDeclare.
    def visitVarDeclare(self, ctx:BKITParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#decl.
    def visitDecl(self, ctx:BKITParser.DeclContext):
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


    # Visit a parse tree produced by BKITParser#function.
    def visitFunction(self, ctx:BKITParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#state_list1.
    def visitState_list1(self, ctx:BKITParser.State_list1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#state_list2.
    def visitState_list2(self, ctx:BKITParser.State_list2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_state.
    def visitAssign_state(self, ctx:BKITParser.Assign_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_state.
    def visitIf_state(self, ctx:BKITParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#iff.
    def visitIff(self, ctx:BKITParser.IffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif.
    def visitElseif(self, ctx:BKITParser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#els.
    def visitEls(self, ctx:BKITParser.ElsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_state.
    def visitFor_state(self, ctx:BKITParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_state.
    def visitWhile_state(self, ctx:BKITParser.While_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_state.
    def visitDo_while_state(self, ctx:BKITParser.Do_while_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_state.
    def visitBreak_state(self, ctx:BKITParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_state.
    def visitContinue_state(self, ctx:BKITParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_state.
    def visitReturn_state(self, ctx:BKITParser.Return_stateContext):
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


    # Visit a parse tree produced by BKITParser#func_state.
    def visitFunc_state(self, ctx:BKITParser.Func_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrDeclare.
    def visitArrDeclare(self, ctx:BKITParser.ArrDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index.
    def visitIndex(self, ctx:BKITParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr.
    def visitArr(self, ctx:BKITParser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#lit.
    def visitLit(self, ctx:BKITParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
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


    # Visit a parse tree produced by BKITParser#rela_operator.
    def visitRela_operator(self, ctx:BKITParser.Rela_operatorContext):
        return self.visitChildren(ctx)



del BKITParser