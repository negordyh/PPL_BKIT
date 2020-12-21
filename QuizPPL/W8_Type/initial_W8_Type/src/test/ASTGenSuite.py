import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test0(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test1(self):
        input = """Var:x=12.e-3;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], FloatLiteral(0.012))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test2(self):
        input = """Var:x,y;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None),
                VarDecl(Id("y"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test3(self):
        input = """Var:x=1,y[1][2];"""
        expect = \
            Program([
                VarDecl(Id('x'), [], IntLiteral(1)),
                VarDecl(Id("y"), [1, 2], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_expr_6(self):
        input = """Function : main 
Body:
expr = expr == 1;
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[], [Assign(Id("expr"), BinaryOp(
                         "==",
                            Id("expr"),
                            IntLiteral(1)))
                     ]])
                     )])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_expr_7(self):
        input = """Function : main 
Body:
expr = -.y;
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[], [Assign(Id("expr"), UnaryOp(
                         "-.",
                            Id("y")))
                     ]])
                     )])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    

    def test_glbDecl_1(self):
        input = """Var : x;"""
        expect = Program(
            [VarDecl(variable=Id(name='x'), varDimen=[], varInit=None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_assignStat_4(self):
        input = """Function : main 
Body:
x[i] = 1;
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[],
                            [Assign(ArrayCell(Id("x"), [Id("i")]),
                                    IntLiteral(1))]
                            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_expr_2(self):
        input = """Function : main 
Body:
expr = expr + 1;
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[],
                            [Assign(Id("expr"),
                                    BinaryOp("+", Id("expr"), IntLiteral(1)))]]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_glbDecl_2(self):
        input = """Var : x, y = 5;"""
        expect = Program([
            VarDecl(variable=Id("x"), varDimen=[], varInit=None),
            VarDecl(variable=Id("y"), varDimen=[], varInit=IntLiteral(5))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    

    def test_glbDecl_5(self):
        input = """Var : x, y = "z";
Var : z = "str";
"""
        expect = Program([VarDecl(Id("x"), [], None),
                          VarDecl(Id("y"), [], StringLiteral("z")),
                          VarDecl(Id("z"), [], StringLiteral("str"))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    

    def test17(self):
        input = """
    Function: main
    Body:
    If a Then
    ElseIf a Then
    EndIf.
    EndBody.
    """
        expect = \
            Program(
                [FuncDecl(
                    Id("main"), [],
                    ([],
                     [If([(Id("a"), [], []), (Id("a"), [], [])], ([], []))]))])

        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test18(self):
        input = """
    Function: main
    Body:
    For (i=1,i>10,1) Do 
    EndFor.
    EndBody.
    """
        expect = \
            Program([
                FuncDecl(
                    Id("main"), [],
                    ([],
                     [For(Id("i"), IntLiteral(1), BinaryOp(">", Id("i"), IntLiteral(10)), IntLiteral(1), ([], []))]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test19(self):
        input = """
    Function: main
    Body:
    For (i=1,i>10,1) Do 
    EndFor.
    Break;
    EndBody.
    """
        expect = \
            Program([
                FuncDecl(
                    Id("main"), [],
                    ([],
                     [For(Id("i"), IntLiteral(1), BinaryOp(">", Id("i"), IntLiteral(10)), IntLiteral(1), ([], [])),
                      Break()])
                )
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test20(self):
        input = """
    Var: a;
    Var: b;
    Var: c;
    """
        expect = \
            Program([
                VarDecl(Id('a'), [], None),
                VarDecl(Id('b'), [], None),
                VarDecl(Id('c'), [], None)
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test21(self):
        input = """
    Var: a[0x123][0o17][0X20][0O71];
    """
        expect = \
            Program([
                VarDecl(Id('a'), [291, 15, 32, 57], None)
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test22(self):
        input = """
    Function: main
    Body:
    EndBody.
    """
        expect = \
            Program([
                FuncDecl(Id('main'), [], ([], []))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test23(self):
        input = """
    Function: main
    Body:
    If a Then
    ElseIf a Then
    ElseIf a Then
    EndIf.
    EndBody.
    """
        expect = \
            Program([
                FuncDecl(Id('main'), [],
                         ([], [If([(Id("a"), [], []), (Id("a"), [], []), (Id("a"), [], [])], ([], []))]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_glbDecl_4(self):
        input = """Var : x, y = "z";
Var : z = "str";
"""
        expect = Program([VarDecl(Id("x"), [], None),
                          VarDecl(Id("y"), [], StringLiteral("z")),
                          VarDecl(Id("z"), [], StringLiteral("str"))
                          ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test25(self):
        input = """
    Function: main
    Body:
    x = 10 + a ;
    Return a+b-c;
    EndBody.
    """
        a = Assign(Id("x"), BinaryOp("+", IntLiteral(10), Id("a")))
        b = Return(BinaryOp("-", BinaryOp("+", Id("a"), Id("b")), Id("c")))
        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [a, b]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test26(self):
        input = """
    Function: main
    Body:
    If a Then
        For (a=a,a,a) Do EndFor.
    EndIf.
    EndBody.
    """
        a = For(Id("a"), Id("a"), Id("a"), Id("a"), ([], []))
        b = If([(Id("a"), [], [a])], ([], []))

        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [b]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test27(self):
        input = """
    Function: main
    Body:
    If a Then 
        If a Then EndIf.
    Else
    EndIf.
    EndBody.
    """
        a = If([(Id("a"), [], [])], ([], []))
        b = If([(Id("a"), [], [a])], ([], []))
        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [b]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test28(self):
        input = """
    Function: main
    Body:
    a[3 + foo(2)] = a[b[2][3]] + 4;
    EndBody.
    """
        a = BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))
        b = ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])
        c = ArrayCell(Id("a"), [a])
        d = ArrayCell(Id("a"), [b])
        e = BinaryOp("+", d, IntLiteral(4))
        f = Assign(c, e)
        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [f]))
            ])

        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

   

    def test32(self):
        input = """
    Function: main
    Body:
    If bool_of_string ("True") Then
        a = int_of_string (read ());
        b = float_of_int (a) +. 2.0;
    EndIf.
    EndBody.
    """
        a = CallExpr(Id("int_of_string"), [CallExpr(Id("read"), [])])
        b = Assign(Id("a"), a)
        c = BinaryOp("+.", CallExpr(Id("float_of_int"),
                                    [Id("a")]), FloatLiteral(2.0))
        d = Assign(Id("b"), c)
        e = CallExpr(Id("bool_of_string"), [StringLiteral("True")])

        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [If([(e, [], [b, d])], ([], []))]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

 

    def test34(self):
        input = """
        Var:x;
        Var:y;
        Function: x
        Body:
        EndBody.
        Function: y
        Body:
        EndBody.
        """
        a = VarDecl(Id("x"), [], None)
        b = VarDecl(Id("y"), [], None)
        c = FuncDecl(Id("x"), [], ([], []))
        d = FuncDecl(Id("y"), [], ([], []))
        expect = \
            Program([
                a, b, c, d
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    

    def test_glbDecl_3(self):
        input = """Var : foo[2][3] = "Okay"; """

        expect = Program([VarDecl(Id("foo"), [2, 3], StringLiteral("Okay"))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_expr_10(self):
        input = """Function : main 
Body:
expr = foo();
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[], [Assign(Id("expr"),
                                        CallExpr(Id("foo"), []))
                                 ]])
                     )])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

   

   

    def test40(self):
        input = """Function: main
Body:
If a==b Then Break;
EndIf.
EndBody."""
        a = BinaryOp("==", Id("a"), Id("b"))
        b = If([(a, [], [Break()])], ([], []))
        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [b]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test41(self):
        input = """Function: main
Body:
For (i=1,i<10,1) Do
    If a==b Then Break;
    EndIf.
EndFor.
EndBody."""
        a = BinaryOp("==", Id("a"), Id("b"))
        b = If([(a, [], [Break()])], ([], []))
        c = BinaryOp("<", Id("i"), IntLiteral(10))
        d = For(Id("i"), IntLiteral(1), c, IntLiteral(1), ([], [b]))
        expect = \
            Program([
                FuncDecl(Id("main"), [], ([], [d]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test42(self):
        input = """Function: foo
Body:
If a==b Then a=b;
ElseIf a==c Then a=c;
ElseIf a==d Then a=d;
ElseIf a==e Then a=e;
ElseIf a==f Then a=f;
Else a=g;
EndIf.
EndBody."""
        a = BinaryOp("==", Id("a"), Id("b"))
        a1 = Assign(Id("a"), Id("b"))
        c = BinaryOp("==", Id("a"), Id("c"))
        c1 = Assign(Id("a"), Id("c"))
        d = BinaryOp("==", Id("a"), Id("d"))
        d1 = Assign(Id("a"), Id("d"))
        e = BinaryOp("==", Id("a"), Id("e"))
        e1 = Assign(Id("a"), Id("e"))
        f = BinaryOp("==", Id("a"), Id("f"))
        f1 = Assign(Id("a"), Id("f"))
        g = Assign(Id("a"), Id("g"))
        h = If([(a, [], [a1]), (c, [], [c1]), (d, [], [d1]),
                (e, [], [e1]), (f, [], [f1])], ([], [g]))
        expect = \
            Program([
                FuncDecl(Id("foo"), [], ([], [h]))
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

   

    def test44(self):
        input = """Var: x,y; Var:z;
Function: main
Body:

EndBody."""
        expect = \
            Program([
                VarDecl(Id("x"), [], None),
                VarDecl(Id("y"), [], None),
                VarDecl(Id("z"), [], None),
                FuncDecl(Id("main"), [], ([], [])),
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test45(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test46(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test47(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test48(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test49(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test50(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test51(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test52(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test53(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test54(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test55(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test56(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test57(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test58(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test59(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test60(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test61(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test62(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test63(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test64(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test65(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test66(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test67(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test68(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test69(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test70(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test71(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test72(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test73(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test74(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test75(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test76(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test77(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test78(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test79(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test80(self):
        input = """Var:x;"""
        expect = \
            Program([
                VarDecl(Id("x"), [], None)
            ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    

      

    def test_expr_12(self):
        input = """Function : main 
Body:
expr = a[i];
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[], [Assign(Id("expr"), ArrayCell(Id("a"), [Id("i")]))
                                 ]])
                     )])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_expr_13(self):
        input = """Function : main 
Body:
expr = a[foo() + 1];
EndBody."""
        expect = Program([
            FuncDecl(Id("main"),
                     [],
                     tuple([[], [Assign(Id("expr"), ArrayCell(Id("a"),
                                                              [BinaryOp("+", CallExpr(Id("foo"), []), IntLiteral(1))]))
                                 ]])
                     )])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))


    def test_program_structure_2(self):
        input = """Var : gbVar = "Hello", var2 = "World";
Var : x = 12;
Function : foo
Body:
EndBody. """
        expect = Program(
            [   VarDecl(Id("gbVar"), [], StringLiteral("Hello")),
                VarDecl(Id("var2"), [], StringLiteral("World")),
                VarDecl(Id("x"), [], IntLiteral(12)),
                FuncDecl(Id("foo"),[],tuple([[],[]]) 
            )])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_program_structure_3(self):
        input = """Var : gbVar = "Hello", var2 = "World";
Var : x = 12;
Function : foo
Body:
EndBody.
Function : main
Body:
EndBody."""
        expect = Program(
            [   VarDecl(Id("gbVar"), [], StringLiteral("Hello")),
                VarDecl(Id("var2"), [], StringLiteral("World")),
                VarDecl(Id("x"), [], IntLiteral(12)),
                FuncDecl(Id("foo"),[],tuple([[],[]])),
                FuncDecl(Id("main"),[],tuple([[],[]]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_assignStat_1(self):
        input = """Function : main 
Body:
x = 1;
EndBody."""
        expect = Program([
                FuncDecl(Id("main"),
                [], 
                tuple([[],[Assign(Id("x"), IntLiteral(1))]]))   
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_assignStat_2(self):
        input = """Function : main 
Body:
x[2] = 1;
EndBody."""
        expect = Program([
                FuncDecl(Id("main"),
                [], 
                tuple([[],
                    [Assign(ArrayCell(Id("x"), [IntLiteral(2)]), 
                        IntLiteral(1))]
                ]))   
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))    
    
    def test_assignStat_3(self):
        input = """Function : main 
Body:
x[2]["i"] = 1;
EndBody."""
        expect = Program([
                FuncDecl(Id("main"),
                [], 
                tuple([[],
                    [Assign(ArrayCell(Id("x"), [IntLiteral(2), StringLiteral("i")]), 
                        IntLiteral(1))]
                ]))   
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))    

    def test_assignStat_4(self):
        input = """Function : main 
Body:
x[i] = 1;
EndBody."""
        expect = Program([
                FuncDecl(Id("main"),
                [], 
                tuple([[],
                    [Assign(ArrayCell(Id("x"), [Id("i")]), 
                        IntLiteral(1))]
                ]))   
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))    

      

     

    def test_expr_1(self):
        input = """Function : main 
Body:
expr = "simple test";
EndBody."""
        expect = Program([
                FuncDecl(Id("main"),
                [], 
                tuple([[],
                    [Assign(Id("expr"), 
                        StringLiteral("simple test"))]
                ]))   
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))  
        

    def test_empty_program303(self):
        input = """**Function: main
            Body:
                x = 10;
                fact (x);
            EndBody.**"""
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_globalvardecl304(self):
        input = """
        Var: a = 10.;
        Var: b[5];
        Var: c[2][3],d = 6, e;"""
        expect = str(Program([
            VarDecl(Id("a"),[],FloatLiteral(10.)),
            VarDecl(Id("b"), [5], None),
            VarDecl(Id("c"), [2,3], None),
            VarDecl(Id("d"), [], IntLiteral(6)),
            VarDecl(Id("e"), [], None)
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_converthex_int305(self):
        input = """
        Var: b[0xFFFF];
        Var: m[4][9];"""
        expect = str(Program([
            VarDecl(Id("b"), [65535], None),
            VarDecl(Id("m"), [4,9], None),
                            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_convertoct_int306(self):
        input = """
                Var: b[0xFFFF];
                Var: c[0O77][9];"""
        expect = str(Program([
            VarDecl(Id("b"), [65535], None),
            VarDecl(Id("c"), [63, 9], None),
                                ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    

    def test_ifstmt320(self):
        input = """Var: n = 9 ;
                Function: main
                     Body:
                         If (n == 0) Then
                                Return 1;
                         EndIf.
                     EndBody."""
        expect = str(Program([
            VarDecl(Id("n"), [], IntLiteral(9)),
            FuncDecl(Id("main"),
                     [],
                     ([], [ If ( [ ( BinaryOp("==", Id("n"), IntLiteral(0)), [], [Return(IntLiteral(1))]) ],
                                    ([], []) )] ))

                     ]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 401))