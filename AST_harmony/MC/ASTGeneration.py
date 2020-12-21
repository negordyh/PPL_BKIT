# Name: Vo Xuan Hau
# Student ID: 1711265
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    
    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        d = []
        for i in ctx.decl():
       	    d = d + self.visit(i)
        return Program(d)
            

    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visit(ctx.var_decl()) if ctx.var_decl() else [self.visit(ctx.func_decl())]
    

    # Visit a parse tree produced by MCParser#var_decl.
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        a = self.visit(ctx.prmt_type())
        result = []
        for i in ctx.var_id():
            result += [VarDecl(i.single_id().ID().getText(),a)] if i.single_id() \
                else [VarDecl(i.arr_id().ID().getText(), ArrayType(int(i.arr_id().INTLIT().getText()),a))]
        return result
        

    # Visit a parse tree produced by MCParser#var_id.
    def visitVar_id(self, ctx:MCParser.Var_idContext):
        pass


    def visitSingle_id(self, ctx:MCParser.Single_idContext):
        pass


    # Visit a parse tree produced by MCParser#arr_id.
    def visitArr_id(self, ctx:MCParser.Arr_idContext):
        pass


    # Visit a parse tree produced by MCParser#prmt_type.
    def visitPrmt_type(self, ctx:MCParser.Prmt_typeContext):
        if ctx.BOOLTYPE():
            return BoolType()
        if ctx.STRINGTYPE():
            return StringType()
        if ctx.FLOATTYPE():
            return FloatType()
        if ctx.INTTYPE():
            return IntType()


    # Visit a parse tree produced by MCParser#fun_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type
        #body: Block
        #ID = Id(ctx.ID().getText())
        #p = self.visit(ctx.paralist()) if ctx.paralist() else []
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paralist()) if ctx.paralist() else [], self.visit(ctx.functype()),self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by MCParser#paralist.
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return [self.visit(i) for i in ctx.paradecl()]
    

    # Visit a parse tree produced by MCParser#functype.
    def visitFunctype(self, ctx:MCParser.FunctypeContext):
        return VoidType() if ctx.VOIDTYPE() else self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MCParser#arr_point_type.
    def visitArr_point_type(self, ctx:MCParser.Arr_point_typeContext):
        return ArrayPointerType(self.visit(ctx.prmt_type()))


    # Visit a parse tree produced by MCParser#paradecl.
    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        return VarDecl(ctx.ID().getText(),self.visit(ctx.prmt_type())) if ctx.getChildCount() == 2 else VarDecl(ctx.ID().getText(),ArrayPointerType(self.visit(ctx.prmt_type())))


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        block = []
        for i in ctx.term():
            block += self.visit(i)
        return Block(block)
        

    # Visit a parse tree produced by MCParser#term.
    def visitTerm(self, ctx:MCParser.TermContext):
        return [self.visit(ctx.stmt())] if ctx.stmt() else self.visit(ctx.var_decl(
            
        ))


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)),self.visit(ctx.stmt(1))) if ctx.ELSE() \
            else If(self.visit(ctx.exp()),self.visit(ctx.stmt(0)))


    # Visit a parse tree produced by MCParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MCParser.Do_while_stmtContext):
        return Dowhile([self.visit(i) for i in ctx.stmt()],self.visit(ctx.exp()))


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return For(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),self.visit(ctx.stmt()))


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()


    # Visit a parse tree produced by MCParser#exp_stmt.
    def visitExp_stmt(self, ctx:MCParser.Exp_stmtContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return BinaryOp(ctx.ASSIGNOP().getText(), self.visit(ctx.exp1()),self.visit(ctx.exp())) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp1())


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return BinaryOp(ctx.OROP().getText(), self.visit(ctx.exp1()),self.visit(ctx.exp2())) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp2())



    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return BinaryOp(ctx.ANDOP().getText(), self.visit(ctx.exp2()),self.visit(ctx.exp3())) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp3())


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp4(0)),self.visit(ctx.exp4(1))) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp4(0))


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return BinaryOp(self.visit(ctx.op4()), self.visit(ctx.exp5(0)),self.visit(ctx.exp5(1))) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp5(0))


    # Visit a parse tree produced by MCParser#op4.
    def visitOp4(self, ctx:MCParser.Op4Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5()),self.visit(ctx.exp6())) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp6())


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return BinaryOp(self.visit(ctx.op6()), self.visit(ctx.exp6()),self.visit(ctx.exp7())) if ctx.getChildCount() == 3 \
            else self.visit(ctx.exp7())


    # Visit a parse tree produced by MCParser#op6.
    def visitOp6(self, ctx:MCParser.Op6Context):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7())) if ctx.getChildCount() == 2 \
            else self.visit(ctx.exp8())


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.exp())) if ctx.getChildCount() == 4 \
            else self.visit(ctx.exp9())



    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visit(ctx.exp()) if ctx.getChildCount() == 3 \
            else self.visit(ctx.operand())



    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visit(ctx.funccall()) if ctx.funccall() else self.visit(ctx.literal())


    # Visit a parse tree produced by MCParser#listeral.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT():
            value = True if ctx.BOOLLIT().getText() == "true" else False
            return BooleanLiteral(value)
        else:
            return Id(ctx.ID().getText())

    
    # Visit a parse tree produced by MCParser#funccall.
    def visitFunccall(self, ctx:MCParser.FunccallContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.paralist_call()) if ctx.paralist_call() else [])
    

    # Visit a parse tree produced by MCParser#paralist_call.
    def visitParalist_call(self, ctx:MCParser.Paralist_callContext):
        return [self.visit(i) for i in ctx.exp()]