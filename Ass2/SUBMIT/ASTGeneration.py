from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    #program: (varDeclare|function)* EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        lstdecl=[]
        for x in range(0,ctx.getChildCount()-1):
            decl=self.visit(ctx.getChild(x))
            if type(decl)==type([]):
                lstdecl+=decl
            else:
                lstdecl.append(decl)
        return Program(lstdecl)

    #varDeclare: VAR COLON decl (COMMA decl)* SEMI;
    def visitVarDeclare(self,ctx:BKITParser.VarDeclareContext):
        return [self.visit(x) for x in ctx.decl()]

    # decl: ID
    # |ID ASSIGN literal
    # |arrDeclare
    # |arrDeclare ASSIGN literal;
    def visitDecl(self,ctx:BKITParser.DeclContext):
        if ctx.getChildCount()==1 and ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],None)
        elif ctx.getChildCount()==1 and ctx.arrDeclare():

            a=ctx.arrDeclare()
            b=[]
            for x in a.index():
                stringg=x.INTLIT().getText()
                if len(stringg)>1:
                    if stringg[1] == 'x' or stringg[1] == 'X':
                        inlit = int(stringg, 16)
                        b.append(inlit)
                    elif stringg[1] == 'o' or stringg[1] == 'O':
                        inlit = int(stringg, 8)
                        b.append(inlit)
                    else:
                        inlit = int(stringg)
                        b.append(inlit)
                else:
                    inlit = int(stringg)
                    b.append(inlit)
            return VarDecl(Id(a.ID().getText()),b,None)
        elif ctx.getChildCount()==3 and ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],self.visit(ctx.literal()))
        else:


            a = ctx.arrDeclare()
            b=[]
            for x in a.index():
                stringg=x.INTLIT().getText()
                if len(stringg)>1:
                    if stringg[1] == 'x' or stringg[1] == 'X':
                        inlit = int(stringg, 16)
                        b.append(inlit)
                    elif stringg[1] == 'o' or stringg[1] == 'O':
                        inlit = int(stringg, 8)
                        b.append(inlit)
                    else:
                        inlit = int(stringg)
                        b.append(inlit)
                else:
                    inlit = int(stringg)
                    b.append(inlit)


            return VarDecl(Id(a.ID().getText()),b,self.visit(ctx.literal()))
    
    #arr: LP lit (COMMA lit)* RP;
    def visitArr(self,ctx:BKITParser.ArrContext):
        return ArrayLiteral([self.visit(x) for x in ctx.lit()])
        
    #lit: literal
    def visitLit(self,ctx:BKITParser.LitContext):
            return self.visit(ctx.literal())
        

    #function: FUNCTION COLON ID (decl (COMMA decl)*)? body;
    def visitFunction(self,ctx:BKITParser.FunctionContext):
        param=[self.visit(x) for x in ctx.decl()]
        return FuncDecl(Id(ctx.ID().getText()),param,self.visit(ctx.body()))

    #body: BODY COLON stmt2 ENDBODY DOT;
    def visitBody(self,ctx:BKITParser.BodyContext):
        return self.visit(ctx.stmt2())
    #arraytype: ID LSB exp RSB (LSB exp RSB)*;
    def visitArraytype(self,ctx:BKITParser.ArraytypeContext):
        exp=[]
        for x in ctx.exp():
            exp+=[self.visit(x)]

        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()),exp)
        else:
            return ArrayCell(self.visit(ctx.func_call()),exp)

    #stmt2: varDeclare*stmt1*;
    def visitStmt2(self,ctx:BKITParser.Stmt2Context):
        if ctx.varDeclare() and ctx.stmt1():
            lst = reduce(lambda x, y: x + y,[self.visit(x) for x in ctx.varDeclare()])
            return (lst ,[self.visit(y) for y in ctx.stmt1()])
        elif ctx.varDeclare():
            lst = reduce(lambda x, y: x + y, [self.visit(x) for x in ctx.varDeclare()])
            return (lst,[])
        elif ctx.stmt1():
            return ([],[self.visit(x) for x in ctx.stmt1()])
        else:
            return ([],[])

    def visitStmt1(self,ctx:BKITParser.Stmt1Context):
        return self.visit(ctx.getChild(0))

    #var_decl_stmt: varDeclare;
    def visitVar_decl_stmt(self, ctx:BKITParser.Var_decl_stmtContext):
        return self.visit(ctx.varDeclare())
    
    #assignment_stmt: value ASSIGN exp SEMI;
    def visitAssignment_stmt(self, ctx:BKITParser.Assignment_stmtContext):
        return Assign(self.visit(ctx.value()),self.visit(ctx.exp()))

    #ifthenStmt: IF exp THEN stmt2 (ELSEIF exp THEN stmt2)* ;
    def visitIfthenStmt(self,ctx:BKITParser.IfthenStmtContext):
        lst1 = [self.visit(x) for x in ctx.exp()]  # kieu Exp
        lst2 = [self.visit(x) for x in ctx.stmt2()]  # kieu list 2 phan tu : var , stmt2

        if ctx.ELSEIF():
            return [(lst1[i],lst2[i] [0], lst2[i] [1])  for i in range(len(lst1)) ]
        else:
            return [(lst1[0],lst2[0] [0], lst2[0] [1])]

    #elseStmt: (ELSE stmt2)? ENDIF DOT ;
    def visitElseStmt(self,ctx:BKITParser.ElseStmtContext):
        if ctx.stmt2():
            lst = self.visit(ctx.stmt2())
            return (lst[0],lst[1])
        else:
            return ([],[])

    #if_stmt: ifthenStmt elseStmt ;
    def visitIf_stmt(self,ctx:BKITParser.If_stmtContext):
        return If(self.visit(ctx.ifthenStmt()),self.visit(ctx.elseStmt()))
    
    # for_stmt: FOR LB ID ASSIGN exp COMMA exp COMMA exp RB DO stmt2 ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        abc = self.visit(ctx.stmt2())
        return For(Id(ctx.ID().getText()),self.visit(ctx.exp(0)),self.visit(ctx.exp(1)),self.visit(ctx.exp(2)),(abc[0],abc[1]))
   
    #while_stmt: WHILE exp DO stmt2 ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        bca = self.visit(ctx.stmt2())
        return While(self.visit(ctx.exp()),(bca[0],bca[1]))
    
    # do_while_stmt: DO stmt2 WHILE exp ENDDO DOT;
    def visitDo_while_stmt(self, ctx:BKITParser.Do_while_stmtContext):
        cba = self.visit(ctx.stmt2())
        return Dowhile((cba[0],cba[1]),self.visit(ctx.exp()))

    #break_stmt: BREAK SEMI;
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return Break()
    
    #continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return Continue()
    
    #call_stmt: func_call SEMI;
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        if ctx.bet():
            return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.bet()))
        else:
            return CallStmt(Id(ctx.ID().getText()),[])

    #return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return(None)

    #iid: ID;
    def visitIid(self, ctx:BKITParser.IidContext):
        return Id(ctx.ID().getText())

    #literal: INTLIT|FLOATLIT|BOOLEAN|STRINGLIT;
    def visitLiteral(self,ctx:BKITParser.LiteralContext):
        if ctx.INTLIT():
            a=ctx.INTLIT().getText()
            inlit=0
            if len(a)>1:
                if a[1]=='x' or a[1]=='X':
                    inlit=int(a,16)
                    return 123
                elif a[1]=='o' or a[1]=='O':
                    inlit=int(a,8)
                else:
                    inlit=int(a)
            else:
                inlit=int(a)
            return IntLiteral(inlit)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLEAN():
            if ctx.BOOLEAN.getText()=='True':
                return BooleanLiteral(True )
            else:
                return BooleanLiteral(False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.array())

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.operand(0))
        elif ctx.SUB() or ctx.SUB_DOT():
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp(0)))
        elif ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp(0)))
        elif ctx.mul() or ctx.div() or ctx.MOD():
            if ctx.MOD():
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
            return BinaryOp(self.visit(ctx.getChild(1)),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        elif ctx.add() or ctx.sub():

            return BinaryOp(self.visit(ctx.getChild(1)),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        elif ctx.AND() or ctx.OR():

            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        else:
            a=self.visit(ctx.getChild(1))
            b=self.visit(ctx.getChild(0))
            c=self.visit(ctx.getChild(2))
            return BinaryOp(a,b,c)

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.getChildCount()==3:
            return self.visit(ctx.exp())
        else:
            if ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visit(ctx.getChild(0))
    
    def visitRela_operator(self,ctx:BKITParser.Rela_operatorContext):
        return ctx.getChild(0).getText()
    def visitMul(self,ctx:BKITParser.MulContext):
        return ctx.getChild(0).getText()
    def visitDiv(self,ctx:BKITParser.DivContext):
        return ctx.getChild(0).getText()
    def visitAdd(self,ctx:BKITParser.AddContext):
        return ctx.getChild(0).getText()
    def visitSub(self,ctx:BKITParser.SubContext):
        return ctx.getChild(0).getText()

    #explist : exp COMMA explist | exp ;
    def visitExplist(self, ctx: BKITParser.ExplistContext):
        if ctx.explist():
            return [self.visit(ctx.exp())] + self.visit(ctx.explist())
        else:
            return [self.visit(ctx.exp())]

    #func_call : ID LB explist? RB ;
    def visitFunc_call(self, ctx: BKITParser.Func_callContext):
        if ctx.explist():
            return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.explist()))
        else:
            return CallExpr(Id(ctx.ID().getText()),[])
    
    
    

 