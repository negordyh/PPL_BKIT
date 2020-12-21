from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *




class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        lstdecl=[]
        for x in range(0,ctx.getChildCount()-1):
            decl=self.visit(ctx.getChild(x))
            if type(decl)==type([]):
                lstdecl+=decl
            else:
                lstdecl.append(decl)



        
        return Program(lstdecl)
    def visitVarDeclare(self,ctx:BKITParser.VarDeclareContext):
        return [self.visit(x) for x in ctx.decl()]


    def visitDecl(self,ctx:BKITParser.DeclContext):
        #return ctx.scalar()
        if ctx.getChildCount()==1 and ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],None)
        elif ctx.getChildCount()==1 and ctx.arrDeclare():

            a=ctx.arrDeclare()
            b=[]
            for x in a.index():
                stringg=x.INT().getText()
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
                stringg=x.INT().getText()
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

    def visitArr(self,ctx:BKITParser.ArrContext):
        return ArrayLiteral([self.visit(x) for x in ctx.lit()])

    def visitLit(self,ctx:BKITParser.LitContext):
        return self.visit(ctx.literal())
    def visitLiteral(self,ctx:BKITParser.LiteralContext):

        if ctx.INT():
            a=ctx.INT().getText()
            inlit=0
            if len(a)>1:
                if a[1]=='x' or a[1]=='X':
                    inlit=int(a,16)

                elif a[1]=='o' or a[1]=='O':
                    inlit=int(a,8)
                else:
                    inlit=int(a)
            else:
                inlit=int(a)
            return IntLiteral(inlit)
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.BOOLEAN():

            if ctx.BOOLEAN().getText()=='True':
                return BooleanLiteral(True )
            else:
                return BooleanLiteral(False)
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        else:
            return self.visit(ctx.arr())
    def visitFunction(self,ctx:BKITParser.FunctionContext):

        param=[self.visit(x) for x in ctx.decl()]
        return FuncDecl(Id(ctx.ID().getText()),param,self.visit(ctx.body()))

    def visitBody(self,ctx:BKITParser.BodyContext):

        return self.visit(ctx.state_list2())
    def visitState_list2(self,ctx:BKITParser.State_list2Context):
        lstdecl = []
        if ctx.varDeclare():
            for x in ctx.varDeclare():
                decl = self.visit(x)
                if type(decl) == type([]):
                    lstdecl += decl
                else:
                    lstdecl.append(decl)
        state=[]
        if ctx.state_list1():
            for x in ctx.state_list1():
                stt = self.visit(x)
                if type(stt) == type([]):
                    state += stt
                else:
                    state.append(stt)
        #a=[self.visit(x) for x in ctx.varDeclare()]
        #b=[(self.visit(x) for x in ctx.state_list1())


        return (lstdecl,state)
    def visitState_list1(self,ctx:BKITParser.State_list1Context):
        return self.visit(ctx.getChild(0))

    def visitWhile_state(self,ctx:BKITParser.While_stateContext):
        return While(self.visit(ctx.exp()),self.visit(ctx.state_list2()))

    def visitExp(self,ctx:BKITParser.ExpContext):

        if ctx.getChildCount()==1:

            return self.visit(ctx.operand())

        elif ctx.I_SUB() or ctx.F_SUB():

            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp(0)))
        elif ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp(0)))
        elif ctx.mul() or ctx.div() or ctx.I_REM():
            if ctx.I_REM():
                return BinaryOp(ctx.I_REM().getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
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

    def visitFunc_call(self,ctx:BKITParser.Func_callContext):
        exp=[]
        for x in ctx.exp():
            exp+=[self.visit(x)]
        return CallExpr(Id(ctx.ID().getText()),exp)

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

    def visitFor_state(self,ctx:BKITParser.For_stateContext):

        ID=Id(ctx.ID().getText())
        exp1=self.visit(ctx.exp(0))
        exp2=self.visit(ctx.exp(1))
        exp3=self.visit(ctx.exp(2))
        state=self.visit(ctx.state_list2())
        return For(ID,exp1,exp2,exp3,state)

    def visitDo_while_state(self,ctx:BKITParser.Do_while_stateContext):
        return Dowhile(self.visit(ctx.state_list2()),self.visit(ctx.exp()))

    def visitBreak_state(self,ctx:BKITParser.Break_stateContext):
        return Break()
    def visitContinue_state(self,ctx:BKITParser.Continue_stateContext):
        return Continue()
    def visitReturn_state(self,ctx:BKITParser.Return_stateContext):
        if ctx.exp():
            return Return(self.visit(ctx.exp()))
        else:
            return Return(None)

    def visitFunc_state(self,ctx:BKITParser.Func_stateContext):
        exp = []
        for x in ctx.exp():
            exp += [self.visit(x)]
        return CallStmt(Id(ctx.ID().getText()), exp)

    def visitAssign_state(self,ctx:BKITParser.Assign_stateContext):
        if ctx.ID():

            return Assign(Id(ctx.ID().getText()),self.visit(ctx.exp()))
        else:
            return Assign(self.visit(ctx.arraytype()),self.visit(ctx.exp()))

    def visitArraytype(self,ctx:BKITParser.ArraytypeContext):
        exp=[]
        for x in ctx.exp():
            exp+=[self.visit(x)]

        if ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()),exp)
        else:
            return ArrayCell(self.visit(ctx.func_call()),exp)

    def visitIf_state(self,ctx:BKITParser.If_stateContext):
        if ctx.els():

            return If(self.visit(ctx.iff()),self.visit(ctx.els()))
        else:

            return If(self.visit(ctx.iff()),([],[]))

    def visitIff(self,ctx:BKITParser.IffContext):

        a=self.visit(ctx.exp())
        b=self.visit(ctx.state_list2())
        lst=(a,b[0],b[1])
        lsst=[lst]


        if ctx.elseif():
            for x in ctx.elseif():
                lsst+=[self.visit(x)]
        return lsst
    def visitElseif(self,ctx:BKITParser.ElseifContext):

        a = self.visit(ctx.exp())
        b = self.visit(ctx.state_list2())
        lst = (a, b[0], b[1])
        return lst
    def visitEls(self,ctx:BKITParser.ElsContext):
        return self.visit(ctx.state_list2())



