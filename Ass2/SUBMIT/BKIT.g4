// Mai Van Duyen 1811756 
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program: (varDeclare|function)* EOF;
//variable declaration
varDeclare: VAR COLON decl (COMMA decl)* SEMI;
//decl: decl1 COMMA decl |decl1 ;
decl: ID
    |ID ASSIGN literal
    |arrDeclare
    |arrDeclare ASSIGN literal;
arrDeclare: ID index*;
index: LSB INTLIT RSB;

parameter : PARAMETER COLON (decl) (COMMA decl)*;

idlist: (ID|arraytype) (COMMA (ID|arraytype))*;

arraytype: ID LSB exp RSB (LSB exp RSB)*;

//function declaration
function: FUNCTION COLON ID (decl (COMMA decl)*)? body;
body: BODY COLON stmt2 ENDBODY DOT;

//statements
stmt1: var_decl_stmt
    | assignment_stmt
    | if_stmt
    | for_stmt
    | while_stmt
    | do_while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt;
stmt2: varDeclare*stmt1*;
////Variable Declaration Statement
var_decl_stmt: varDeclare;
////Assignment Statement
assignment_stmt: value ASSIGN exp SEMI;
value: iid | arraytype;
//// The if Statement
ifthenStmt: IF exp THEN stmt2 (ELSEIF exp THEN stmt2)* ;
elseStmt: (ELSE stmt2)? ENDIF DOT ;
if_stmt: ifthenStmt elseStmt ;
////The for Statement
for_stmt: FOR LB ID ASSIGN exp COMMA exp COMMA exp RB DO stmt2 ENDFOR DOT;
////The while Statement
while_stmt: WHILE exp DO stmt2 ENDWHILE DOT;
////The do while Statement
do_while_stmt: DO stmt2 WHILE exp ENDDO DOT;
////The break Statement
break_stmt: BREAK SEMI;
//// The continue Statement
continue_stmt: CONTINUE SEMI;
//// The call Statement
call_stmt: ID LB bet? RB SEMI;
bet: exp(COMMA exp)*;
//// The return Statement
return_stmt: RETURN exp? SEMI;

//Expression
exp: operand
    |(SUB|SUB_DOT) exp
    |NOT exp
    |exp (mul|div|MOD)exp
    |exp (add|sub) exp
    |exp (AND|OR) exp
    |operand rela_operator operand;
operand: LB exp RB|ID| func_call|arraytype| literal;
rela_operator: EQ|NOT_EQ_INT|LT|GT|LTE|GTE|NOT_EQ_FLOAT|LT_DOT|GT_DOT|LTE_DOT|GTE_DOT;
// exp: operand EQ|NOT_EQ_INT|LT|GT|LTE|GTE|NOT_EQ_FLOAT|LT_DOT|GT_DOT|LTE_DOT|GTE_DOT operand | exp1;
// exp1: exp1 (SUB|SUB_DOT) exp2|exp2 ;
// exp2: NOT exp2 | exp3;
// exp3: exp3 MUL exp4 
//     | exp3 MUL_DOT exp4 
//     | exp3 DIV exp4 
//     | exp3 DIV_DOT exp4
//     | exp3 MOD exp4
//     | exp4;
// exp4:  exp4 ADD exp5 
//     | exp4 ADD_DOT exp5
//     | exp4 SUB exp5
//     | exp4 SUB_DOT exp5
//     | exp5;
// exp5: exp5 AND exp6 
//     | exp5 OR exp6 
//     | exp6;
// exp6: operand;


//function call
func_call : ID LB explist? RB ; //callexpr
explist : exp COMMA explist | exp ;

//Comment
BLOCKCOM: '**'('*'?(~[*])+)*'**' -> skip;
WS : [ \f\n\r\t]+ -> skip; // skip spaces, tabs, newlines

//ID
ID: [a-z]+[0-9a-zA-Z'_]*;
iid: ID;

//Keywords
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';


//Operators
ASSIGN:'=';
ADD: '+';
ADD_DOT: '+.';
SUB: '-';
SUB_DOT: '-.';
MUL: '*';
MUL_DOT: '*.';
DIV: '\\';
DIV_DOT: '\\.';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ_INT: '!=';
LT : '<' ;
GT : '>' ;
LTE: '<=';
GTE: '>=';
NOT_EQ_FLOAT: '=/=';
LT_DOT: '<.';
GT_DOT: '>.';
LTE_DOT: '<=.';
GTE_DOT: '>=.';

add: ADD|ADD_DOT;
sub: SUB|SUB_DOT;
mul: MUL|MUL_DOT;
div: DIV|DIV_DOT;
//Separators
LB: '('; 
RB: ')'; 
LP: '{'; 
RP: '}'; 
LSB: '['; 
RSB: ']'; 

SEMI: ';'; 
COMMA: ','; 
COLON: ':'; 
DOT: '.'; 

//Literals
////Integer
literal: INTLIT|FLOATLIT|BOOLEAN|STRINGLIT;
INTLIT : DEC|Hexa|Octal;
    DEC : [1-9][0-9]*|'0';
    Hexa: '0'('x'|'X')[0]*[1-9A-F]+[0-9A-F]*;
    Octal: '0'('o'|'O')[0]*[1-7]+[0-7]*;
////Float
FLOATLIT: INTLIT FLDECIMAL?FLEXPONENT?;
fragment FLDECIMAL: ('.') DEC?;
fragment FLEXPONENT:('e'|'E')(('+'|'-')?)DEC;


////Boolean
BOOLEAN: TRUE|FALSE;
////Array
arr: LP lit (COMMA lit)* RP;
lit: literal;
////String
STRINGLIT :'"' (ESC | ~[\b\t\f\r\n\\"'] | [']["] )* '"'
{
    self.text = self.text[1:-1]
};
fragment ESC: '\\' ["\\bfnrt];


//UNCLOSE STRING
UNCLOSE_STRING: '"' (ESC | ~[\b\t\f\r\n\\"'] | [']["] )*
{
    raise UncloseString(self.text[1:])
};
//ILLEGAL ESCAPE
ILLEGAL_ESCAPE:'"' (ESC | ~[\b\f\n\r\t"'\\])* ('\\' ~[bfnrt"'\\] | [\b\f\t"'\\])
{
    raise IllegalEscape(self.text[1:])
};
//ERROR CHAR
ERROR_CHAR: .
{
    raise ErrorToken(self.text)
};
//UNTERMINATED COMMENT
UNTERMINATED_COMMENT: '**'('*'?(~[*])+)*;


























