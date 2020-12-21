import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_missing_body_decl(self):
        """Missing Body:"""
        input = """Function: main
        Parameter: a, b, c[1][2]
        Var: x = "sdasdas"; EndBody ."""
        expect = "Error on line 3 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_missing_endbody_decl(self):
        """Missing EndBody."""
        input = """Function: main
        Parameter: a, c[1] Body:
        Var: x = "sdasdas";"""
        expect = "Error on line 3 col 27: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_var_declare_position01(self):
        input = """
        Var: a = 0xFFFF;
        Var: b[] = {1,2,3};
        """
        expect = """Error on line 3 col 15: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_var_declare_position02(self):
        input = """
        Var: a = 0xFFFF;
        Var: b[3][2] = {{}};
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_var_declare01(self):
        """Test var declaration with function call assignment"""
        input = """Function: main
        Parameter: a, c[1] Body: Var: x = how(); EndBody. """
        expect = "Error on line 2 col 42: how"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_var_declare02(self):
        """Test composite var declaration"""
        input = """Var: x[how[3]] = 3; """
        expect = "Error on line 1 col 7: how"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_var_declare03(self):
        """Test composite var declaration"""
        input = """Var: x[2][2+3*3] = {{2,3},{2,3}}; """
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_declare04(self):
        input = """
        Var: b = -123412;
        """
        expect = """Error on line 2 col 17: -"""
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_var_declare04(self):
        input = """
        Var: b = -123412;
        """
        expect = """Error on line 2 col 17: -"""
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_comment01(self):
        """Test single line comment """
        input = """Var: x[2][3] = 2, **comment Var: x = 2;** y = "True"; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_comment02(self):
        """Test multi line comment"""
        input = """Var: x[2][3] = 2, **comment 
        Var: x = 2;
        x = 3;** y = "True"; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_simple_program02(self):
        """Test simple program"""
        input = """Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5) Do
        a[i] = b +. 1.0;
        i = i + 1;
        EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_simple_program03(self):
        """Test simple program"""
        input = """Function: foo
        Body:
            While ((i < 5) == (3 < 2 + 5*4)) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.   
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_relational_op01(self):
        """Test relational op"""
        input = """ Function: hi 
        Body: Var:x = 2; x=(x == 3) < (x \ 2 * 2 <= 4); EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_program(self):
        """Test a program from specification"""
        input = \
        """ Var: x;
        Function: fact
            Parameter: n
            Body:
                Var: x = 2;
                If n == 0 Then
                  Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact (x);
            EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_call01(self):
        input = """
        Function: f_111___222
        Parameter :a,b,c, d = 10
        Body:

        EndBody.
        """
        expect = """Error on line 3 col 28: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_function_call02(self):
        input = """
        Function: f_111___222
        Parameter : a[0xAAAAAA123456][0O11232131]
        Body:

        EndBody.
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_program01(self):
        """Test function call program"""
        input = \
        """Function: how Body: If bool_of_string ("True") Then
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            EndIf. EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_intlit_in_vardecl01(self):
        """Test intlit in var decl"""
        input = """Function: how Body: Var: x[2][3]; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_intlit_in_vardecl02(self):
        """Test type other than intlit in var decl"""
        input = """Function: how Body: Var: x[3][True]; EndBody."""
        expect = "Error on line 1 col 30: True"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_intlit_in_vardecl03(self):
        """Test intlit in var decl"""
        input = """Function: how Body: Var: x[3][0o125]; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_intlit_in_vardecl04(self):
        """Test intlit in var decl"""
        input = """Function: how Body: Var: x[1283712837][0X125]; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_function_call03(self):
        """Test function call"""
        input = """Function: how Body: print("howhowhowhw"); EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_break_outside_loop01(self):
        """Test break call outside loop"""
        input = """Function: how Body:
            Break;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_var_declare05(self):
        """Test var decl"""
        input = """Function: how Body:
            Var: x, y, Var;
            Body: EndBody.
        EndBody."""
        expect = "Error on line 2 col 23: Var"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_var_declare06(self):
        """Test var decl"""
        input = """Function: how Body:
            Var: x,;
            Body: EndBody.
        EndBody."""
        expect = "Error on line 2 col 19: ;"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_var_declare07(self):
        """Test var decl"""
        input = """Function: how Body:
            Var x = 3;
            Body: EndBody.
        EndBody."""
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_duplicate_parameter_decl(self):
        """Test duplicate parameter"""
        input = """Function: how Parameter: x Parameter: y Body:
            Var x = 3;
            Body: EndBody.
        EndBody."""
        expect = "Error on line 1 col 27: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_var_declare08(self):
        """Test var decl"""
        input = """Function: how Body:
            Var: x= 2 - 5 * 4;
            Body: EndBody.
        EndBody."""
        expect = "Error on line 2 col 22: -"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_var_declare09(self):
        """Test var decl of specification"""
        input = """Function: how Body: Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_var_declare10(self):
        """Test var decl of specification"""
        input = """Function: how Body: Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10]; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_var_declare10(self):
        """Test var decl of specification"""
        input = """Function: how Body: Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10]; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_function_decl(self):
        input = """
        Var: x=5,a,b=5, a[4] = {1,2,3,{1}};
        Function: fact
        Parameter: a,b,c
        Body:
            
        EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_function_decl02(self):
        """Test duplicate body"""
        input = """Function: how Body: Var: x = 2; EndBody. Body: Var: y = 3; y = "True"; EndBody."""
        expect = "Error on line 1 col 41: Body"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function_decl04(self):
        input = """
        Var: x=5,a,b=5, a[4] = {1,2,3,{1}};
        Function: fact
        Parameter: a[10][2],a_bbbb, a[1]
        Body:
            
        EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_var_3(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        Function: fact
        Parameter: a[10][2],a_bbbb, a[1]
        Body:
            
        EndBody.

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_var_4(self):
        input = """
        Var: a,b,c = {1,2,3};        
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_var_9(self):
        input = """
        Var: b = {1,2,3};
        Var: c = {1,2,{2}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_name_1(self):
        input = """
        Function: _foo ** wrong identifier **
        Parameter: a,,b,c
        Body:

        EndBody.
        """
        expect = "_"
        self.assertTrue(TestParser.checkParser(input, expect, 239))
    
    def test_name_2(self):
        input = """
        Function: foo_123
        Parameter: A,b,c
        Body:

        EndBody.
        """
        expect = "A"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_name_3(self):
        input = """
        Function: foo_123
        Parameter:
        Body:
            abc;
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_name_4(self):
        input = """
        Function: f____OOOOOOO__0000000000
        Parameter: abc, a[10][10][10][10][10][10]
        Body:

        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_name_5(self):
        input = """
        Function: f____OOOOOOO__0000000000
        Body:
        
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_name_6(self):
        input = """
        Function: f____OOOOOOO__0000000000______,
        parameter :a,b,c
        Body:
        
        EndBody.
        """
        expect = """Error on line 2 col 48: ,"""
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_name_7(self):
        input = """
        Function: f_111___222
        Parameter :a,b,c, d = 10
        Body:

        EndBody.
        """
        expect = """Error on line 3 col 28: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_name_8(self):
        input = """
        Function: f_111___222
        Parameter : a[0xAAAAAA123456][0O11232131]
        Body:

        EndBody.
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))
    
    def test_name_9(self):
        input = """
        Function: function_name
        Parameter : a[0xAAAAAA123456][0O11232131], b[10[10]]
        Body:

        EndBody.
        """
        expect = """Error on line 3 col 55: ["""
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_name_10(self):
        input = """
        Function: f_111___222
        Parameter : a[0xAAAAAA123456][0O11232131], Parameter
        Body:

        EndBody.
        """
        expect = """Error on line 3 col 51: Parameter"""
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_assign_1(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            a[3 + foo(foo(2+x,4.\. y) ) + foo(10)] = a[b[9][3]] + 4;
            foo(2+x,4.\. y); 
            goo ();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_assign_2(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            a[3 + foo(foo(2+x,4.\. y) ) + foo(10)] = a[b[9][3]] + 4;
            foo(2+x,4.\. y); 
            goo (goo (goo (goo (goo ()))));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_assign_3(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            a[3 + foo(foo(2+x,4.\. y) ) + foo(10)] = foo(foo(6));
            foo(2+x,4.\. y); 
            goo (goo (goo (goo (goo ()))));
            arrray[array[10] + foo() + abc + "string"] = "string";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_assign_4(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            arrray[array[10] + foo() + abc + "string"];
        EndBody.
        """
        expect = """Error on line 6 col 54: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_assign_5(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            arrray[array[10] + foo() + abc + "string" && abc || bcd +. ({1,2,3})] = 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_assign_7(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            arrray[array[10] + foo() + abc + "string" && abc || bcd +. ({1,2,3})] = 1
        EndBody.
        """
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_assign_8(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            Var: a = 6, foo[10][10], a = "string";
            arrray[array[10] + foo() + abc + "string" && abc || bcd +. ({1,2,3})] = 1;
            arrray[array[10] + 1] = 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_assign_9(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            Var: a = 6, foo[10][10], a = "string";
            arrray[array[10] + foo() + abc + "string" && abc || bcd +. ({1,2,3})] = 1;
            arrray[array[10] + _1] = 1;
        EndBody.
        """
        expect = "_"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_assign_10(self):
        input = """
        Function: foo
        Parameter: a,b,c, a[10][10]
        Body:
            Var: a = 6, foo[10][10];
            Var: a = 6, foo[10][10], a = "string";
            arrray[array[10] + foo() + abc + "string" && abc || bcd +. ({1,2,3})] = 1;
            arrray[()] = 1;
        EndBody.
        """
        expect = "Error on line 8 col 20: )"
        self.assertTrue(TestParser.checkParser(input,expect,257))


    def test_mix_1(self):
        input = """
        Function: mix_test
        Body:
            Break;
            Break;
            Break;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 258))

    def test_mix_10(self):
        input = """
        Function: mix_test
        Body:
            
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 259))

    def test_for_3(self):
        input = """
        Function: loop_test
        Body:
            For(i = 0, a == b) Do
                If a[foo() + b] Then
                    b = c;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "Error on line 4 col 29: )"
        self.assertTrue(TestParser.checkParser(input,expect, 260))

    def test_while_statement03(self):
        """Test while staments"""
        input = """Function: how Body:
                While (x > 3) Do get(x); EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_while_statement04(self):
        """Test while staments"""
        input = """Function: how Body:
                While (x > 3 || (y != x)) Do print(x); EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_while_statement05(self):
        """Test while staments"""
        input = """Function: how Body:
                While (isPrime(x)) Do x = x + 1; print(x); EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_do_while_statement01(self):
        """Test wrong close do while"""
        input = """Function: how Body:
                Do x = x + 1; print(x); While True EndWhile.
            EndBody."""
        expect = "Error on line 2 col 51: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_do_while_statement02(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do x = x + 1; print(x); While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_do_while_statement03(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do print(x); While (x*2 > 3) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_do_while_statement04(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do print(x); While (x > 3 || (y != x)) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_do_while_statement05(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do print(x); While isPrime(x) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))


    def test_for_statement05(self):
        """Test for staments"""
        input = """Function: how Body:
                For (i = 1, i < 56, 1) Do
                    print(i);
                    For (k= 0,k<3,1) Do
                        k = k+1;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_for_statement06(self):
        """Test for staments"""
        input = """Function: how Body:
                For (i = get(2), i < 56, 1) Do
                    If i == 3 Then i = i \ 2; Else Return; EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_for_statement07(self):
        """Test for staments"""
        input = """Function: how Body:
                For (i = 1024, i > get("json"), -3) Do
                    For (k= 0,k<3,1) Do
                        If k == 3 Then k = k \ 2; Else Return; EndIf.
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_for_statement08(self):
        """Test for staments"""
        input = """Function: how Body:
                For (i = 1024, i > 3, get("json")) Do
                    Var: x; x = 3;
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_do_while_statement06(self):
        """Test wrong close do while"""
        input = """Function: how Body:
                Do x = x + 1; While True Do x = get(); EndWhile. While True EndWhile.
            EndBody."""
        expect = "Error on line 2 col 76: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_do_while_statement07(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do x = x + 1; While True Do x = get(); EndWhile. While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_do_while_statement08(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do Do print(x); While (x\\2 > 3) EndDo. While (x*2 > 3) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_do_while_statement09(self):
        """Test do while statement"""
        input = """Function: how Body:
                Do 
                    While (x > 3 || (y != x)) Do
                        x= x+2;
                        While (a * 3 == 2) Do
                            a = a + x;
                            print(x);
                        EndWhile.
                    EndWhile.
                While (x > 3 || (y != x)) EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_break01(self):
        """Test break statement"""
        input = """Function: how Body:
                Do x = x + 1; If x == 3 Then Break; EndIf. While True Do x = get(); EndWhile. While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_break02(self):
        """Test break statement"""
        input = """Function: how Body:
                Do Break; While True Do x = get(); EndWhile. While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_break03(self):
        """Test break statement"""
        input = """Function: how Break; Body:
                Do While True EndDo.
            EndBody."""
        expect = "Error on line 1 col 14: Break"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_continue01(self):
        """Test continue statement"""
        input = """Function: how Body:
                Do x = x + 1; If x == 3 Then Continue; EndIf. While True Do x = get(); EndWhile. While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_continue02(self):
        """Test continue statement"""
        input = """Function: how Body:
                Do Continue; While True Do x = get(); EndWhile. While True EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_exp01(self):
        """Test expression uses"""
        input = """Function: how Body: x = (x-2)*y; EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_exp02(self):
        """Test expression uses"""
        input = """Function: how Body: y = 0x567 * (0o124 - 15 \ 3); EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_exp03(self):
        """Test expression uses"""
        input = """Function: how Body: y = 0x567 * (0o124 - 15 \ 3); EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_var_declare_position03(self):
        """Var declaration position outside function"""
        input = """Function: main
        Parameter: a, c[1] Body:
        a = "True";
        Var: x = "sdasdas"; EndBody. Var: b;"""
        expect = "Error on line 4 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_var_declare_position04(self):
        """Var wrong If close token"""
        input = """Function: main
        Parameter: a, c[1] Body:
        Var: x = "sdasdas"; a = "True";
        If x == a Then x = x - a; While True Do Var: l = True; EndDo. EndIf. EndBody."""
        expect = "Error on line 4 col 63: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_var_declare11(self):
        """Test var declaration with function call assignment"""
        input = """Var: a, b, c= {2}, d; Function: main
        Parameter: a, c[1] Body: Var: x = how(); EndBody. """
        expect = "Error on line 2 col 42: how"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_comment03(self):
        """Test inline comment """
        input = """Var: x[2][3] = 2, **comment If True Then Var: x = 2; EndIf.** y = "True"; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_comment04(self):
        """Test multi line comment"""
        input = """**This do what** Var: x[2][3] = 2, y = "True"; **Some notes**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test_while_statement09(self):
        """Test while staments"""
        input = """Function: how Body:
                While (x > 3 || (y != x)) Do
                    x= x+2;
                    While (a * 3 == 2) Do
                        a = a + x;
                        print(x);
                    EndWhile.
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_return03(self):
        """Test return statement"""
        input = """Function: how Return; Body:
                Do While True EndDo.
            EndBody."""
        expect = "Error on line 1 col 14: Return"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    
    def test_function_decl06(self):
        """Test empty body """
        input = """Function: how Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_function_decl08(self):
        """Test function declaration """
        input = """Function: how Body:
                Var: x;
                x = get("https");
                If x == 0 Then Return;
                    ElseIf x == 1 Then Return get("this");
                    ElseIf x == 2 Then Return 2;
                    ElseIf x == 3 Then Return;
                    Else Return;
                    Else x = 1; EndIf.
            EndBody."""
        expect = "Error on line 9 col 20: Else"
        self.assertTrue(TestParser.checkParser(input,expect,293))
        
    def test_exp07(self):
        """Test expression uses"""
        input = """Function: how Body: y = (x == y) || True; True == True; EndBody."""
        expect = "Error on line 1 col 42: True"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_exp08(self):
        """Test expression uses"""
        input = """Function: how Body: y == x[fibonacci(15) + 2 * 3][int_of_string("0x223")] - 2; EndBody."""
        expect = "Error on line 1 col 22: =="
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_function_call06(self):
        """Test function call"""
        input = """Function: how Body: print(int_of_string("0x2333202");); EndBody."""
        expect = "Error on line 1 col 52: ;"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_function_call07(self):
        """Test function call"""
        input = """Function: how Body: print(int_of_string("0x2333202"); EndBody."""
        expect = "Error on line 1 col 52: ;"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_function_call08(self):
        """Test function call"""
        input = """Function: how Body: print(int_of_string("0x2333202")) = 2; EndBody."""
        expect = "Error on line 1 col 54: ="
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_relational_op03(self):
        """Test relational op"""
        input = """ Function: hi 
        Body: Var:x = 2; x=(x =/= 3) = (x \. 2 * 2 <= 4) && True; EndBody. """
        expect = "Error on line 2 col 37: ="
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_relational_op04(self):
        """Test relational op"""
        input = """ Function: hi 
        Body: Var:x = 2; x == (x =/= 3) != (x <. 4.); EndBody. """
        expect = "Error on line 2 col 27: =="
        self.assertTrue(TestParser.checkParser(input,expect,300))
    