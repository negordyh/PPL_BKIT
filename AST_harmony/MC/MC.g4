// Name: Vo Xuan Hau
// Student ID: 1711265
// MC.g4
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: decl+ EOF;
decl: var_decl | func_decl;

//variable declaration
var_decl: prmt_type var_id (COMMA var_id)* SEMI;
//id_list: var| var COMMA id_list;
var_id: single_id | arr_id;
single_id: ID;
arr_id: ID LSB INTLIT RSB;
prmt_type: BOOLTYPE | STRINGTYPE | FLOATTYPE | INTTYPE;

//function declaration
func_decl: functype ID LB paralist? RB block_stmt;
paralist: paradecl (COMMA paradecl)*;
functype: prmt_type | arr_point_type | VOIDTYPE;
arr_point_type: prmt_type LSB RSB;
//paralist: paradecl | paradecl COMMA paralist;
paradecl: prmt_type ID | prmt_type ID LSB RSB;


//statements
//// The block statement
block_stmt: LP term* RP;
//block_list: term | term block_list;
term: stmt | var_decl;

stmt: if_stmt
    | do_while_stmt
    | for_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    | exp_stmt
    | block_stmt;
//// The if Statement
if_stmt: IF LB exp RB stmt (ELSE stmt)?;
//else_if_stmt: ELSE stmt;
////The do while Statement
do_while_stmt: DO stmt+ WHILE exp SEMI;
//stmt_list: stmt | stmt stmt_list;
////The for Statement
for_stmt: FOR LB exp SEMI exp SEMI exp RB stmt;
////The break Statement
break_stmt: BREAK SEMI;
//// The continue Statement
continue_stmt: CONTINUE SEMI;
//// The return Statement
return_stmt: RETURN exp? SEMI;
//// The expression Statement
exp_stmt: exp SEMI;

// Expression
exp: exp1 ASSIGNOP exp | exp1;
exp1: exp1 OROP exp2 | exp2;
exp2: exp2 ANDOP exp3 | exp3;
exp3: exp4 EQUALOP exp4 | exp4 NOTEQUALOP exp4 | exp4;
exp4: exp5 op4 exp5 | exp5;
    op4: LESSOP | LEOREQUOP | GREATEROP | GROREQUOP;
exp5: exp5 ADDOP exp6 | exp5 SUBOP exp6 | exp6;
exp6: exp6 op6 exp7 | exp7;
    op6: DIVOP | MULOP | MODOP;
exp7: SUBOP exp7 | NOTOP exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: LB exp RB | operand;
operand: literal | funccall;
literal: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | ID;
////fumction call
funccall: ID LB paralist_call? RB;
paralist_call: exp ( COMMA exp)*;

//Comment
BLOCKCOM:  '/*' .*? '*/' -> skip;
LINECOM:  '//' ~[\r\n]* -> skip;
WS : [ \f\n\r\t]+ -> skip ; // skip spaces, tabs, newlines

////bool literal
BOOLLIT: TRUE|FALSE;

//Keywords
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';

BOOLTYPE: 'boolean';
STRINGTYPE: 'string';
FLOATTYPE: 'float';
INTTYPE: 'int' ;
VOIDTYPE: 'void' ;


//Literals
////int
INTLIT: [0-9]+;
//floating point
FLOATLIT: FRAC|EXP;
    FRAC: INTLIT? '.' INTLIT|INTLIT '.' INTLIT?;
    EXP: NUMBER [Ee] SUBOP? INTLIT;
    NUMBER: FRAC | INTLIT;
//string
STRINGLIT: '"' (ESC | ~[\b\f\n\r\t"\\])* '"'{
    self.text = self.text[1:-1]
};
fragment ESC: '\\' ["\\bfnrt];

//Separators
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';' ;
COMMA: ',';

//Operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NOTOP: '!';
OROP: '||';
ANDOP: '&&';
NOTEQUALOP: '!=';
EQUALOP: '==';
LESSOP: '<';
GREATEROP: '>';
LEOREQUOP: '<=';
GROREQUOP: '>=';
ASSIGNOP: '=';

//ID
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//UNCLOSE STRING
UNCLOSE_STRING: '"' (ESC | ~[\b\f\n\r\t"\\])*
{
    self.text = self.text[1:]
};

//ILLEGAL ESCAPE
ILLEGAL_ESCAPE: '"' (ESC | ~[\b\f\n\r\t"\\])* ( '\\' ~[bfnrt"\\] | [\b\f\t"\\])
{
    self.text = self.text[1:]
};

//ERROR CHAR
ERROR_CHAR: .;