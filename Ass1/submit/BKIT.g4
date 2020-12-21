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

program: (var_decl|func_decl)* EOF;
//variable declaration
var_decl: VAR COLON (ID|arr_decl) (ASSIGN(literal))? (COMMA(ID|arr_decl) (ASSIGN(literal|))?)* SEMI;

arr_decl: ID indexes;
indexes: index|index indexes;
index: LSB INTLIT RSB;

parameter : PARAMETER COLON (idlist);

idlist: (ID|arraytype) (COMMA (ID|arraytype))*;

arraytype: ID LSB exp RSB (LSB exp RSB)*;

//function declaration
func_decl: FUNCTION COLON ID parameter? body;
body: BODY COLON var_decl* stmt2 ENDBODY DOT;

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
stmt2: var_decl*stmt1*;
////Variable Declaration Statement
var_decl_stmt: var_decl;
////Assignment Statement
assignment_stmt: (ID | arraytype) ASSIGN exp SEMI;
//// The if Statement
if_stmt: IF exp THEN stmt2
        (ELSEIF exp THEN stmt2)*
        (ELSE stmt1)?
        ENDIF DOT;
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
call_stmt: func_call SEMI;
//// The return Statement
return_stmt: RETURN exp? SEMI;

//Expression
exp: operand
    |(SUB|SUB_DOT)exp
    |NOT exp
    |exp (mul|div|MOD)exp
    |exp (add|sub) exp
    |exp (AND|OR) exp
    |operand rela_operator operand;
operand: LB exp RB|ID| func_call|arraytype| literal;
//function call
func_call :ID LB (exp(COMMA exp)*)? RB;

//Comment
BLOCKCOM: '**'('*'?(~[*])+)*'**' -> skip;
WS : [ \f\n\r\t]+ -> skip; // skip spaces, tabs, newlines

//ID
ID: [a-z]+[0-9a-zA-Z'_]*;

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
rela_operator: EQ|NOT_EQ_INT|LT|GT|LTE|GTE|NOT_EQ_FLOAT|LT_DOT|GT_DOT|LTE_DOT|GTE_DOT;

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
literal: INTLIT|FLOATLIT|BOOLEAN|STRINGLIT|array;
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
array: LP lit? RP;
lit: literal COMMA lit|literal;
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


























