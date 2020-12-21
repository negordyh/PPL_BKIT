import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("abc_12Agv@","abc_12Agv,Error Token @",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("123duyen","123,duyen,<EOF>",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("Aduyen123","Error Token A",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.checkLexeme("aA12_ghJk21$readf","aA12_ghJk21,Error Token $",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.checkLexeme("1811756van_duyen1811756","1811756,van_duyen1811756,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.checkLexeme("Varr 3","Var,r,3,<EOF>",108))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.checkLexeme("0t","0,t,<EOF>",109))
    def test_identifier_10(self):
        self.assertTrue(TestLexer.checkLexeme("a_A","a_A,<EOF>",110))

    def test_keywords(self):
        """checkLexeme whitespace"""
        self.assertTrue(TestLexer.checkLexeme("Body Break Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False EndDo"
                        ,"Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>", 111))

    def test_operators(self):
        """checkLexeme unclose string"""
        self.assertTrue(TestLexer.checkLexeme("+ +. - -. * *. \ \. % ! && || == != < > <= >= =/= <. >. <=. >=."
                        , "+,+.,-,-.,*,*.,\,\.,%,!,&&,||,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>", 112))
    def test_seperators_1(self):
        self.assertTrue(TestLexer.checkLexeme("( ) [ ] : . , ; { }", "(,),[,],:,.,,,;,{,},<EOF>", 113))
    def test_seperators_2(self):
        self.assertTrue(TestLexer.checkLexeme("(van duyen)", "(,van,duyen,),<EOF>", 114))

    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("123abc","123,abc,<EOF>",115))
    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("128312412","128312412,<EOF>",116))
    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("1283 12412","1283,12412,<EOF>",117))
    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("0x123Fgh","0x123F,gh,<EOF>",118))
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("0 0X123Fgh","0,0X123F,gh,<EOF>",119))
    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("0xFDAa 0O123","0xFDA,a,0O123,<EOF>",120))
    def test_integer_7(self):
        self.assertTrue(TestLexer.checkLexeme("0o123","0o123,<EOF>",121))
    def test_integer_8(self):
        self.assertTrue(TestLexer.checkLexeme("0o1238","0o123,8,<EOF>",122))
    def test_integer_9(self):
        self.assertTrue(TestLexer.checkLexeme("0O1238duyen","0O123,8,duyen,<EOF>",123))
    def test_integer_10(self):
        self.assertTrue(TestLexer.checkLexeme("0X123ABG123456789","0X123AB,Error Token G",124))


    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("10.e2","10.e2,<EOF>",125))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("10.","10.,<EOF>",126))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("10e3","10e3,<EOF>",127))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("10e-3","10e-3,<EOF>",128))
    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("10.E+3","10.E+3,<EOF>",129))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("12.25","12.25,<EOF>",130))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("10.25E-24","10.25E-24,<EOF>",131))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("123.23e+23abc","123.23e+23,abc,<EOF>",132))
    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("12000.abc","12000.,abc,<EOF>",133))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("1.26e2E3","1.26e2,Error Token E",134))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme('"This i\'"s string"', 'This i\'"s string,<EOF>',135))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(r'"This is\n string"', r"This is\n string,<EOF>",136))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(r'"This\t is\r string"', r'This\t is\r string,<EOF>',137))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme("\"This\\b is \'\" string \" ",'This\\b is \'\" string ,<EOF>',138))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""",139))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(r'"This is string"', r'This is string,<EOF>',140))
        
    def test_escape_1(self):
        """checkLexeme unclose string"""
        self.assertTrue(TestLexer.checkLexeme('"this is string"', "this is string,<EOF>",141))
    def test_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(r"""
        "Formfeed   \f"
        """,r'Formfeed   \f,<EOF>',142))
    def test_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            "Tab        \t"
            """, r'Tab        \t,<EOF>',143))

    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            illegal: "\a"
            """,r'''illegal,:,Illegal Escape In String: \a''',144))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",145))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            " A Hi Hi \n\k"
            """, r"Illegal Escape In String:  A Hi Hi \n\k",146))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme('"van\\k duyen "', "Illegal Escape In String: van\k",147))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme('"\\kvan\\k duyen "', "Illegal Escape In String: \k",148))
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme('"van duyen \m"', "Illegal Escape In String: van duyen \m",149))
    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","""123,Illegal Escape In String: 123a\\m""",150))

    def test_unclose_string_1(self):
        """checkLexeme unclose string"""
        self.assertTrue(TestLexer.checkLexeme('"this is unclose string', "Unclosed String: this is unclose string",151))
    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.checkLexeme('this is unclose "string', "this,is,unclose,Unclosed String: string",152))
    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.checkLexeme('"this is unclose" "string', "this is unclose,Unclosed String: string",153))
    def test_unclose_string_4(self):
        self.assertTrue(TestLexer.checkLexeme('this is unclose " " string', "this,is,unclose, ,string,<EOF>",154))
    def test_unclose_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            " abcxyz
            """, r"""Unclosed String:  abcxyz""",
            155))

    def test_whitespace_1(self):
        """checkLexeme whitespace"""
        self.assertTrue(TestLexer.checkLexeme(" \n\t", "<EOF>", 156))
    def test_whitespace_2(self):
        self.assertTrue(TestLexer.checkLexeme("\t", "<EOF>", 157))
    def test_whitespace_3(self):
        self.assertTrue(TestLexer.checkLexeme("\n", "<EOF>", 158))
    def test_whitespace_4(self):
        self.assertTrue(TestLexer.checkLexeme(" \t \n \r", "<EOF>", 159))
    def test_whitespace_5(self):
        self.assertTrue(TestLexer.checkLexeme("van\nduyen \t\r", "van,duyen,<EOF>", 160))

    def test_comments_1(self):
        """checkLexeme comment"""
        self.assertTrue(TestLexer.checkLexeme("**vanduyen**","<EOF>",161))
    def test_comments_2(self):
        self.assertTrue(TestLexer.checkLexeme("""**
                                                  * van duyen
                                                  * 1811756
                                                  **""","<EOF>",162))
    def test_comments_3(self):
        self.assertTrue(TestLexer.checkLexeme("*****","*,<EOF>",163))
    def test_comments_4(self):
        self.assertTrue(TestLexer.checkLexeme("** duyen**0x123","0x123,<EOF>",164))
    def test_comments_5(self):
        self.assertTrue(TestLexer.checkLexeme("********", "<EOF>", 165))
    def test_comments_6(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a block comment \n", "Unterminated Comment", 166))
    
    def test_error_char_1(self):
        """checkLexeme error char"""
        self.assertTrue(TestLexer.checkLexeme("0x123 duyen $", "0x123,duyen,Error Token $", 167))
    def test_error_char_2(self):
        self.assertTrue(TestLexer.checkLexeme("van1234_duyen@", "van1234_duyen,Error Token @", 168))
    def test_error_char_3(self):
        self.assertTrue(TestLexer.checkLexeme("+=!\@@@", "+,=,!,\,Error Token @", 169))
    def test_error_char_4(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x; ^", "Var,:,x,;,Error Token ^", 170))

    
    def test_complex_171(self):
        self.assertTrue(TestLexer.checkLexeme("while(1) i = i+1;","while,(,1,),i,=,i,+,1,;,<EOF>",171))

    def test_complex_172(self):
        input = "Var: b[2][3] = {{    2,3,4}, {4,5  ,6}};"
        expect = "Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_complex_173(self):
        input = "Var: m, n[10];"
        expect = "Var,:,m,,,n,[,10,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_complex_174(self):
        input = "Var: c = {1,2,3,0x123,0o123,0.23e-4}"
        expect = "Var,:,c,=,{,1,,,2,,,3,,,0x123,,,0o123,,,0.23e-4,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_complex_175(self):
        input = "Var: a = 5;"
        expect = "Var,:,a,=,5,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_complex_176(self):
        input = """Var: x;
Function: Fact
Parameter: n
Body:
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
EndBody."""
        expect = "Var,:,x,;,Function,:,Error Token F"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_complex_177(self):
        self.assertTrue(TestLexer.checkLexeme("if(a[i]=true) return;","if,(,a,[,i,],=,true,),return,;,<EOF>",177))

    def test_complex_178(self):
        input = "Var: x = 6/2"
        expect = "Var,:,x,=,6,Error Token /"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_complex_179(self):
        input = "Var: x = 6\\2*4+2"
        expect = "Var,:,x,=,6,\\,2,*,4,+,2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_complex_180(self):
        input = "Var: x= 6.e+23-.6.75E-78"
        expect = "Var,:,x,=,6.e+23,-.,6.75E-78,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_complex_181(self):
        input = "Var: x= 0x123FA-0O123"
        expect = "Var,:,x,=,0x123FA,-,0O123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_complex_182(self):
        input = "Var: x= (0x123FA-0O123) + (1235 \ 256 * (125\\5));"
        expect = "Var,:,x,=,(,0x123FA,-,0O123,),+,(,1235,\,256,*,(,125,\,5,),),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_complex_183(self):
        input = "Var: x= (0.E+12+.(12.35e-2-.25.6*.(125.\\5.));"
        expect = "Var,:,x,=,(,0.E+12,+.,(,12.35e-2,-.,25.6,*.,(,125.,\\,5.,),),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_complex_184(self):
        self.assertTrue(TestLexer.checkLexeme("a(a+1);","a,(,a,+,1,),;,<EOF>",184))

    def test_complex_185(self):
        self.assertTrue(TestLexer.checkLexeme("do while true;","do,while,true,;,<EOF>",185))

    def test_complex_186(self):
        self.assertTrue(TestLexer.checkLexeme("foo(s[i],x);","foo,(,s,[,i,],,,x,),;,<EOF>",186))

    def test_complex_187(self):
        self.assertTrue(TestLexer.checkLexeme("for (int i;;) i++","for,(,int,i,;,;,),i,+,+,<EOF>",187))

    def test_complex_188(self):
        input = """foo (2 + x, 4. \. y);
goo ();"""
        expect = "foo,(,2,+,x,,,4.,\.,y,),;,goo,(,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_complex_189(self):
        input = " vanduyen_210()12.e[123]"
        expect = "vanduyen_210,(,),12.,e,[,123,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_complex_190(self):
        input = "123.e1.e{[123] \"\'\"\" }duyen"
        expect = "123.e1,.,e,{,[,123,],\'\",},duyen,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_complex_191(self):
        input = "0\nt = [\"RU\", \"UR\"]\nWhile (i < len(s)):\n "
        expect = "0,t,=,[,RU,,,UR,],While,(,i,<,len,(,s,),),:,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_complex_192(self):
        input = "if len(k) == 1:\n        return 1\n    if len(k) % 2 == 1:\n   return 1 + f(k[0:len(k)-1])"
        expect = "if,len,(,k,),==,1,:,return,1,if,len,(,k,),%,2,==,1,:,return,1,+,f,(,k,[,0,:,len,(,k,),-,1,],),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_complex_193(self):
        input = "[n, m] = nput().strip().split()))\ns = [abs(l[i+1] - l[i])"
        expect = "[,n,,,m,],=,nput,(,),.,strip,(,),.,split,(,),),),s,=,[,abs,(,l,[,i,+,1,],-,l,[,i,],),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_complex_194(self):(TestLexer.checkLexeme("foo(){return;}","foo,(,),{,return,;,},<EOF>",194))

    def test_complex_195(self):
        input = "for i in range(len(a)):\n        for j in range(len(a[0]))"
        expect = "for,i,in,range,(,len,(,a,),),:,for,j,in,range,(,len,(,a,[,0,],),),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_complex_196(self):
        input = "int n,m;\n    cin >> n >> m;\n    int arr[n + 1];\n "
        expect = "int,n,,,m,;,cin,>,>,n,>,>,m,;,int,arr,[,n,+,1,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_complex_197(self):
        input = "pair<int, int> b)\n{\n    if (a.first < b.first)\n"
        expect = "pair,<,int,,,int,>,b,),{,if,(,a,.,first,<,b,.,first,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_complex_198(self):
        input = "Var: fl = 0.12e123; Var: a[[fl][0x123F,0O256]];"
        expect = "Var,:,fl,=,0.12e123,;,Var,:,a,[,[,fl,],[,0x123F,,,0O256,],],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_complex_199(self):
        input = " for (long long i = 0; i < n; i ++)\n        cin >> a1[i];\n"
        expect = "for,(,long,long,i,=,0,;,i,<,n,;,i,+,+,),cin,>,>,a1,[,i,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test_complex_200(self):
        input = "Var: duyen = new Duyen();\n"
        expect = "Var,:,duyen,=,new,Error Token D"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))
