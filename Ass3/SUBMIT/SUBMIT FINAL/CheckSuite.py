import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    
    def test0(self):
        input = """
        Var: x[10], y, x;
        Function: foo
        Parameter: x
        Body:
            Var: y;
        EndBody.
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test1(self):
        input = """Function: main
                   Body:
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_diff_numofparam_stmt(self):
        input = """Function: main
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_diff_numofparam_expr(self):
        input = """Function: main
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_undeclared_function_use_ast(self):
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_diff_numofparam_expr_use_ast(self):
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_diff_numofparam_stmt_use_ast(self):
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test7(self):
        input = """Var: test;
        Function: main
            Parameter: x
            Body:
            x = test[0];
            EndBody.
"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("test"), [IntLiteral(0)])))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test8(self):
        input = """
        Var: a;

        Function: main
        Body:
        Var: a;
        If 2>1 Then 
            a=1;
        EndIf.
        a=1.1;
        Return;
        EndBody.   
"""
        expect = str(TypeMismatchInStatement(Assign(Id("a"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test9(self):
        input = """
        Var: a,b,c=1;
        Var: a=1;
"""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test10(self):
        input = """
        Var: a,b,c=1;

        Function: a
        Body:
        Return;
        EndBody.
"""
        expect = str(Redeclared(Function(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test11(self):
        input = """
        Var: a,b,c=1;

        Function: main
        Parameter: a,a
        Body:
        Return;
        EndBody.
"""
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test12(self):
        input = """
        Var: a,b,c=1;

        Function: main
        Parameter: a,b
        Body:
        Var: b=1;
        Return;
        EndBody.
"""
        expect = str(Redeclared(Variable(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test13(self):
        input = """
        Function: main
        Parameter: a
        Body:
        b=1;
        Return;
        EndBody.
"""
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test14(self):
        input = """
        Function: main
        Parameter: a
        Body:
        b();
        Return;
        EndBody.
"""
        expect = str(Undeclared(Function(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test15(self):
        input = """
        Function: main
        Parameter: a
        Body:
        a=1;
        a="h";
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id("a"), StringLiteral("h"))))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test16(self):
        input = """
        Function: main
        Parameter: a
        Body:
        a=1+"h";
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(1), StringLiteral("h"))))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test17(self):
        input = """
        Function: main
        Parameter: a
        Body:
        a=1+"h";
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInExpression(BinaryOp("+", IntLiteral(1), StringLiteral("h"))))
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test18(self):
        input = """
        Function: main
        Body:
        Var: a[1][1][1]={{{"h"}}};
        a[1][3][1]=1;
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInStatement(
            Assign(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(3), IntLiteral(1)]), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_var_3(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: main
            Parameter: b,c
            Body:
                a = -d - 2;
            EndBody.
            
            """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_var_4(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: foo
            Parameter: b,c
            Body:
                Return 1;
            EndBody.
                       
            Function: main
            Parameter: b,c
            Body:
                a = foo(d,10);
            EndBody.
            
            """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_var_5(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: foo
            Parameter: b,c
            Body:
                Return 1;
            EndBody.
                       
            Function: main
            Parameter: b,c
            Body:
                a = arr[10];
            EndBody.
            
            """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared_var_6(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: foo
            Parameter: b,c
            Body:
                Return;
            EndBody.
                       
            Function: main
            Parameter: b,c
            Body:
                foo(d,12);
            EndBody.
            
            """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test23(self):
        input = """
        Function: main
        Body:
        Var: a=1,x;
        a=foo(x);
        EndBody.

        Function: foo
        Parameter: x
        Body:
        Return 1;
        EndBody.

"""
        expect = str(TypeCannotBeInferred(Assign(Id("a"), CallExpr(Id("foo"), [Id("x")]))))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test24(self):
        input = """
        Function: main
        Body:
        foo(x);
        EndBody.

        Function: foo
        Parameter: x
        Body:
        Return;
        EndBody.

"""
        expect = str(Undeclared(Identifier(), "x"))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test25(self):
        input = """
        Function: main
        Body:
        Var: x;
        foo(x);
        EndBody.

        Function: foo
        Parameter: x
        Body:
        Return;
        EndBody.

"""
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"), [Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test26(self):
        input = """
        Function: main
        Body:
        Var: x,y;
        x=1.1;
        If 1>2 Then Var: x; x=1;
        Else y=x;
        EndIf.
        y=1;
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInStatement(Assign(Id("y"), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test427(self):
        input = r"""
        Function: main
            Body:
            Var: x[3], y[4];
            x[1] = 3;
            y[2] = x[1];
            y = x;
            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(y),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test428(self):
        input = r"""
        Function: foo
        Parameter: x
            Body:
            Var: z = 5;
            z = x;
            EndBody.
        Function: main
            Body:
            Var: x = 5;
            x = foo(3.5);
            EndBody.
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(3.5)])"
        self.assertTrue(TestChecker.test(input, expect, 428))


    def test29(self):
        input = """
        Function: main
        Body:
        Var: x[1][2];
        x[1]=True;
        Return;
        EndBody.
"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("x"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test30(self):
        input = """
        Function: main
        Body:
        Var: a[1][2];
        a[1][2]=1;
        a[1][2]=1.1;
        Return;
        EndBody.    
"""
        expect = str(
            TypeMismatchInStatement(Assign(ArrayCell(Id("a"), [IntLiteral(1), IntLiteral(2)]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test31(self):
        input = """
        Function: foo
        Parameter: a,b[1][2]
        Body:
        a=1;
        b[1][2]=a;
        Return;
        EndBody.

        Function: main
        Body:
        Var: a,b[1][2],c;
        foo(a,{{1,4}});
        a=1.1;
        Return;
        EndBody.     
"""
        expect = str(TypeMismatchInStatement(Assign(Id("a"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test32(self):
        input = """
        Function: foo
        Parameter: a,b[1][2]
        Body:
        a=1;
        b[1][2]=a;
        Return b;
        EndBody.

        Function: main
        Body:
        Var: a,b[1][2],c;
        c=foo(a,{{1,2}})[1][1];
        c=1.1;
        Return;
        EndBody.     
"""
        expect = str(TypeMismatchInStatement(Assign(Id("c"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test33(self):
        input = """
        Function: foo
        Parameter: a,b[1][2]
        Body:
        a=1;
        b[1][2]=a;
        Return b;
        EndBody.

        Function: main
        Body:
        Var: a,b[1][2],c;
        c=foo(a,{{1,2}})[1][1];
        c=1.1;
        Return;
        EndBody.     
"""
        expect = str(TypeMismatchInStatement(Assign(Id("c"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test34(self):
        input = """
        Function: foo
        Parameter: a,b[1][2]
        Body:
        a=1;
        b[1][2]=a;
        Return b;
        EndBody.

        Function: main
        Body:
        Var: a,b[1][2],c;
        c=foo(a,{{1,2}})[1][1];
        c=1.1;
        Return;
        EndBody.     
"""
        expect = str(TypeMismatchInStatement(Assign(Id("c"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_infer_5(self):
        input = r"""
        Var: a;
        Function: main
            Body:
                a = foo();
            EndBody.
        Function: foo
            Body:
            EndBody.
        """
        expect = "Type Cannot Be Inferred: Assign(Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 435))   

    def test_infer_6(self):
        input = r"""
        Var: a[10], arr[10];
        Function: main
            Body:
                a = arr;
            EndBody.
        """
        expect = "Type Cannot Be Inferred: Assign(Id(a),Id(arr))"
        self.assertTrue(TestChecker.test(input, expect, 436))  

    def test_infer_7(self):
        input = r"""
        Var: x;
        Function: foo
        Parameter: a
        Body:
        EndBody.

        Function: main
            Body:
            foo(6);
            foo(x);
            x = 5.0

            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),FloatLiteral(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))   

    def test_infer_8(self):
        input = r"""
        Var: x, y;
        Function: foo
        Parameter: a
        Body:
        Var: x;
        x = 6.0;
        y = x;
        EndBody.

        Function: main
            Body:
            foo(6);
            foo(x);
            x = y;

            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 438)) 

    def test_infer_9(self):
        input = r"""
        Var: x, y;
        Function: foo
        Parameter: a
        Body:
        Var: x[10];
        x[5] = 6.0;
        y = x[6];
        EndBody.

        Function: main
            Body:
            foo(6);
            foo(x);
            x = y;

            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 439))   

    def test_infer_10(self):
        input = r"""
        Var: x, y;
        Function: foo
        Parameter: a
        Body:
        EndBody.

        Function: main
            Body:
            foo(6);
            x = foo(5);

            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),CallExpr(Id(foo),[IntLiteral(5)]))"
        self.assertTrue(TestChecker.test(input, expect, 440))  

    def test41(self):
        input = """
        Function: main
        Parameter: v,b
        Body:
        Var: a[1][2];
        a[1]=True;
        EndBody.
"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id("a"), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test42(self):
        input = """
        Function: main
        Parameter: a[1][1],b
        Body:
        a[b][1]=1;
        b=1.1;
        EndBody.


"""
        expect = str(TypeMismatchInStatement(Assign(Id("b"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test43(self):
        input = """ Function: main
                    Body:
                    EndBody.

                    Function: main
                    Body: EndBody.
                    """
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test44(self):
        input = """ Function: main
                    Parameter: x,y
                    Body:
                    EndBody.

                    Function: main
                    Parameter: z
                    Body: EndBody.
                    """
        expect = str(Redeclared(Function(), "main"))
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test45(self):
        input = """ Var: x , y;
                    Var: y;
                    Function: main
                    Body: EndBody.
                    """
        expect = str(Redeclared(Variable(), "y"))
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test46(self):
        input = """ Var: x , y;
                    Function: main
                    Parameter: x, z
                    Body:
                        Var: z = 2;
                    EndBody.
                    """
        expect = str(Redeclared(Variable(), 'z'))
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test47(self):
        input = """ Var: x , y;
                    Function: main
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                    EndBody.

                    Function: foo
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_debug06(self):
        input = """ Var: x , y;
                    Function: main
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                    EndBody.

                    Function: foo
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                    EndBody.

                    Function: bar
                    Parameter: y
                    Body: EndBody.

                    Function: foo
                    Parameter: x
                    Body: EndBody.
                    """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_debug07(self):
        input = """ Var: x , y;
                    Function: foo
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                    EndBody.
                    """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_debug08(self):
        # TODO need to be checked again
        input = """ Var: x , y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = x;
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id('y'), Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_debug09(self):
        input = """ Var: x , y;
                    Function: main
                    Parameter: x, z
                    Body:
                        Var: y = 2, c;
                        Var: y = True;
                    EndBody.
                    """
        expect = str(Redeclared(Variable(), 'y'))
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_debug10(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = 2;
                        y = True;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_debug11(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = 2;
                    EndBody.

                    Function: foo
                    Parameter: z
                    Body:
                        y = True;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_debug12(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = 2;
                    EndBody.

                    Function: foo
                    Parameter: y
                    Body:
                        y = True;
                        z = 2;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(), 'z'))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_debug13(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = 2;
                    EndBody.

                    Function: foo
                    Parameter: x
                    Body:
                        y = 14;
                    EndBody.

                    Function: bar
                    Parameter: x[1]
                    Body:
                        y = 68;
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_debug14(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        y = 2;
                    EndBody.

                    Function: foo
                    Parameter: x
                    Body:
                        y = 14;
                    EndBody.

                    Function: bar
                    Parameter: x[1]
                    Body:
                        y = "how";
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), StringLiteral("how"))))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_debug15(self):
        input = """ Var: x, y;
                    Function: main
                    Parameter: x, z
                    Body:
                        x = 2;
                    EndBody.

                    Function: foo
                    Parameter: x
                    Body:
                        x = 14;
                    EndBody.

                    Function: bar
                    Parameter: z
                    Body:
                        x = "how";
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_debug16(self):
        input = """ Var: x, y;

                    Function: foo
                    Parameter: x
                    Body:
                        x = 14;
                    EndBody.

                    Function: main
                    Parameter: x, z
                    Body:
                        x = 2;
                    EndBody.

                    Function: bar
                    Parameter: z
                    Body:
                        x = "how";
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_debug17(self):
        input = """ Function: main
                    Body:
                        Var: y = 2;
                        y = True;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_debug18(self):
        input = """ Function: main
                    Body:
                        Var: y = 2;
                        y = {1, 2};
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([IntLiteral(1), IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_debug19(self):
        input = """ Function: main
                    Body:
                        Var: y = True;
                        y = {{1, 2}, {3,4}};
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])]))))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_debug20(self):
        input = """ Function: main
                    Body:
                        Var: y[2][2];
                        y = {{1, 2}, {3,4}};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_debug21(self):
        input = """ Function: main
                    Body:
                        Var: y[3];
                        y = {True, False, True};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_debug22(self):
        input = """ Function: main
                    Body:
                        Var: y[2][2][2];
                        y = {{{"h", "o"}, {"h", "o"}},{{"h", "o"}, {"h", "o"}}};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_debug23(self):
        input = """ Function: main
                    Body:
                        Var: y[2];
                        y = {0X123, 0x124};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_debug24(self):
        input = """ Function: main
                    Body:
                        Var: y[2];
                        y = {0X123, 0x124, 0x125};
                    EndBody.
                    """
        expect = str(
            TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([IntLiteral(291), IntLiteral(292), IntLiteral(293)]))))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_debug25(self):
        input = """ Function: main
                    Body:
                        Var: y[2];
                        y = {0X123, 0x124};
                        y = {True, False};
                    EndBody.
                    """
        expect = str(
            TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]))))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_debug26(self):
        input = """ Var: y[2];
                    Function: main
                    Body:
                        y = {0X123, 0x124};
                        y = {True, False};
                    EndBody.
                    """
        expect = str(
            TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]))))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_debug27(self):
        input = """ Var: y[2];
                    Function: foo
                    Body:
                        y = {True, False};
                    EndBody.

                    Function: main
                    Body:
                        y = {0X123, 0x124};
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([IntLiteral(0x123), IntLiteral(0x124)]))))
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_debug28(self):
        input = """ Var: y[2][2];
                    Function: foo
                    Body:
                        y = {0X123, 0x124};                    
                    EndBody.

                    Function: main
                    Body:
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([IntLiteral(0x123), IntLiteral(0x124)]))))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_debug29(self):
        input = """ Var: y[2][2];
                    Function: foo
                    Body:
                        y = {{0X123, 0x124}, {1, 2}};                    
                    EndBody.

                    Function: main
                    Body:
                        Var: y[2];
                        y = {0X123, 0x124};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_debug30(self):
        input = """ Var: y[2][2];
                    Function: foo
                    Body:
                        y = {{0X123, 0x124}, {1, 2}};                    
                    EndBody.

                    Function: main
                    Parameter: y[2]
                    Body:
                        y = {0X123, 0x124};
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_debug31(self):
        input = """ Var: y[2];
                    Function: main
                    Parameter: z[2]
                    Body:
                        z = {1, 2};
                        z = y;
                    EndBody.

                    Function: foo
                    Body:
                        y = {"h", "o"};
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), ArrayLiteral([StringLiteral("h"), StringLiteral("o")]))))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_debug32(self):
        input = """ Var: y[2];
                    Function: main
                    Parameter: z
                    Body:
                        z = "st";
                        z = y;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('z'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_debug33(self):
        input = """ Var: y[2];
                    Function: main
                    Parameter: z[2]
                    Body:
                        z = {True, False};
                        z = {False, True};
                        y = {2, 3};
                        z = y;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('z'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_debug34(self):
        input = """ Var: y[2][2];
                    Function: main
                    Parameter: z[2][2]
                    Body:
                        y = {{2, 3},{4, 5}};
                        y = {{0x123, 0x124},{0x1, 0x2}};
                        z = {{"s", "t"}, {"m", "t"}};
                        z = y;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('z'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_debug35(self):
        input = """ Var: y[2][2];
                    Function: main
                    Parameter: z[2][2]
                    Body:
                        z = y;
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(Id('z'), Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_debug36(self):
        input = """ Var: x, foo;
                    Function: main
                    Body: EndBody.

                    Function: foo
                    Body: EndBody.
                    """
        expect = str(Redeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_debug37(self):
        input = """ Var: x, foo;
                    Function: main
                    Body:
                        Var: main;
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_debug38(self):
        input = """ Var: x;
                    Function: main
                    Body:
                        x = 2;
                        x = foo;
                    EndBody.

                    Function: foo
                    Body: EndBody.
                    """
        expect = str(Undeclared(Identifier(), 'foo'))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_debug39(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        x = {{1 , 2},{0x12 , 0o22}};
                        x[1][2] = 2;
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_debug40(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        x = {{1 , 2},{0x12 , 0o22}};
                        x[1] = 2;
                    EndBody.
                    """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_debug41(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        x = {{1 , 2},{0x12 , 0o22}};
                        x[1][2] = True;
                    EndBody.
                    """
        expect = str(
            TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(1), IntLiteral(2)]), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_debug42(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        x[1][2] = True;
                        x = {{1 , 2},{0x12 , 0o22}};
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(0x12), IntLiteral(0o22)])]))))
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_debug43(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        Var: y = 69;
                        x[1][1] = 3;
                        y = x[1][1];
                    EndBody.
                    """
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_debug44(self):
        input = """ Var: x[2][2];
                    Function: main
                    Body:
                        Var: y[2][2];
                        x[1][1] = y[1][0];
                    EndBody.
                    """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id('x'), [IntLiteral(1), IntLiteral(1)]),
                                                 ArrayCell(Id('y'), [IntLiteral(1), IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test87(self):
        input = r"""
        Function: main
        Body:
            Var: a = 5;
            a = 6 + 5.5;
        EndBody.
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(6),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test88(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: foo
            Parameter: a,b,c
            Body:
                Var: f = 10;
                Var: x;
                a = 1;
                b = 2;
                main(1,2,x);
                Return 1;
            EndBody.

            Function: foo1
            Body:
                Return 1;
            EndBody.

            Function: main
            Parameter: a, b, c
            Body:
                foo1();
                Return ;
            EndBody.

            """
        expect = str(TypeCannotBeInferred(CallStmt(Id('main'),[IntLiteral(1),IntLiteral(2),Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 488))

    

    def test89(self):
        input = """ 
                    Function: main
                    Body:
                    Var: a;
                        If True Then Var:x;
                            While True Do  
                                If False Then a=1; EndIf.
                            EndWhile.
                        EndIf.
                        a=1.1;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(Assign(Id("a"), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    

    def test91(self):
        input = """ Var: main;
                    Function: abc
                    Parameter:x[1][2]
                    Body:
                    Return x;
                    EndBody.

                    Function: foo
                    Parameter:x
                    Body:
                    Return;
                    EndBody.
                    """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test92(self):
        input = """
                    Function: main
                    Parameter:x[1][2]
                    Body:
                    x[1][1]=1;
                    Return;
                    EndBody.

                    Function: foo
                    Parameter:x
                    Body:
                    main(x);
                    Return;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("x")])))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_undeclared_var_1(self):
        """Simple program: main"""
        input = """
        Var: b;
        Var: c;

        Function: foo
        Body:
            b = 10;
            b = a + c;
        EndBody.

        Function: main
        Body:
        EndBody.

        """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_func_6(self):
        input = r"""
            Function : print
            Parameter : x
            Body:
                Return;
            EndBody.
            Function: ma
            Body:
                Var : value = 12345;
                Return value;
            EndBody.
            Function: main
            Parameter : x, y
            Body: 
                print(m); 
                Return 0;
            EndBody.
            """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_undeclared_var_20(self):
        """Simple program: main"""
        input = """
            Var: a;
            Function: foo
            Parameter: a,b,c
            Body:
                Return 1;
                main(1,2,3);
            EndBody.
            
            Function: main
            Parameter: a, b, c
            Body:
                Return 1;
            EndBody.
            
            """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_mismatch_stmt_2(self):
        input = r"""
        Function: main
        Body:
            Var: a = 5;
            a = 6.5;
        EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(a),FloatLiteral(6.5))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_mismatch_expr(self):
        input = r"""
        Function: main
        Body:
            Var: a = 5;
            a = 6 + 5.5;
        EndBody.
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(6),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_infer_array(self):
        input = r"""
        Function: main
            Body:
            Var: x, y, z[5];
            z[x] = 1;
            y = 2.2;
            x = y;
            EndBody.
        """
        expect = "Type Mismatch In Statement: Assign(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_infer_array_2(self):
        input = r"""
        Function: foo
            Parameter: x
            Body:
                Var: z[5];
                z[x] = 2;
            EndBody.
        Function: main
            Body:
            foo(3.5);
            EndBody.
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[FloatLiteral(3.5)])"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_lit_2(self):
        input = r"""
        Var: x[3];
        Function: main
            Body:
            Var: a;
            x[1] = 5;
            a = x[1];
            EndBody.
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))

   