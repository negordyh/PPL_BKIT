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

//program  : VAR COLON ID SEMI EOF varDeclare;
program: ( varDeclare|function )* EOF ;
//varDeclare: 'Var' ':' (ID|arrDeclare) ('='(literal))?  (','(ID|arrDeclare) ('='(literal|))?)* ';';
varDeclare: VAR COLON decl (COMMA decl)* SEMI;
//decl: decl1 COMMA decl |decl1 ;
decl: ID
    |ID ASSIGN literal
    |arrDeclare
    |arrDeclare ASSIGN literal;



//| ID ASSIGN literal;

parameter : 'Parameter' ':' (decl) (COMMA decl)* ;



idlist: (ID|arraytype) (',' (ID|arraytype))*;

arraytype: (ID|func_call) '[' exp ']' ('[' exp ']')*;

function: 'Function' ':' ID ('Parameter' ':' decl (COMMA decl)*)? body;
body: 'Body' ':'

        state_list2
        'EndBody' '.';
state_list1:assign_state|if_state|for_state|while_state|do_while_state|break_state|continue_state|return_state|func_state;
state_list2:varDeclare*state_list1*;
assign_state: (ID|arraytype) '=' exp ';';


if_state: iff  els? ENDIF '.';
iff:IF exp THEN state_list2 elseif*;
elseif :ELSEIF exp THEN state_list2;
els:ELSE state_list2;

for_state :FOR  '(' ID '=' exp ',' exp ',' exp')' DO state_list2 ENDFOR '.';
while_state: WHILE exp DO state_list2 ENDWHILE '.';
do_while_state: DO state_list2 WHILE exp ENDDO'.';
break_state: BREAK ';';
continue_state: CONTINUE';';
return_state: RETURN exp?';';

exp:operand
    | (I_SUB|F_SUB)exp
    | NOT exp
    | exp (mul|div|I_REM)exp
    |exp (add|sub) exp
    |exp (AND|OR) exp
    |exp rela_operator exp;
operand: LP exp RP|ID| func_call |arraytype |  literal;

func_call :ID '(' (exp(','exp)*)?')';
func_state: ID '(' (exp(','exp)*)?')' ';';

arrDeclare: ID index*;
index: LSB INT RSB;

arr: LB lit (COMMA lit)* RB;
lit: literal|arr;
literal: INT |FLOAT|BOOLEAN|STRING|arr;



WS : [ \t\r\n\f\b]+ -> skip ;
add: I_ADD|F_ADD;
sub: I_SUB|F_SUB;
mul: I_MUL|F_MUL;
div: I_DIV|F_DIV;
COMMENT: '**'('*'?(~[*])+)*'**'->skip ;
ID: [a-z]+[0-9a-zA-Z'_]*;
//OPERATORS:'+'|'+.'|'-'|'-.'|'*'|'*.'|'\\'|'\\.'|'%'|'&&'|'||'|'! ='|'<'|'>'|'>='|'= / ='|'< .'|'<= .'|'>= .';
ASSIGN:'=';
I_SUB: '-';
I_ADD: '+';
I_MUL: '*';
I_DIV: '\\';
I_REM: '%';
F_SUB: '-.';
F_ADD: '+.';
F_MUL: '*.';
F_DIV: '\\.';
NOT: '!';
AND: '&&';
OR: '||';
//Relational operators
EQUAL: '==';
I_NOTEQUAL: '!=';
I_LESSTHAN: '<';
I_GREATERTHAN: '>';
I_LTOE: '<=';
I_GTOE: '>=';
F_NOTEQUAL: '=/=';
F_LESSTHAN: '<.';
F_GREATERTHAN: '>.';
F_LTOE: '<=.';
F_GTOE: '>=.';
rela_operator:
EQUAL|I_NOTEQUAL|I_LESSTHAN|I_GREATERTHAN|I_LTOE|I_GTOE
|F_NOTEQUAL|F_LESSTHAN|F_GREATERTHAN|F_LTOE|F_GTOE;
//SEPARATORS:'('|')'|'['|']'|'.'|','|';'|'{'|'}';
LP: '(';
RP: ')';
LSB: '[';
RSB: ']';
COLON: ':';
DOT: '.';
COMMA: ',';
SEMI: ';';
LB: '{';
RB: '}';
INT : DEC|Hexa|Octal;
DEC : [1-9][0-9]*|'0';
Hexa: '0'('x'|'X')[0]*[1-9A-F]+[0-9A-F]*;
Octal: '0'('o'|'O')[0]*[1-7]+[0-7]*;

FLOAT: DEC[.][0-9]*EXP?|[0][.][0-9]*[1-9][0-9]*EXP?|DEC EXP;
fragment EXP: [eE][+-]?[0-9]*;
BOOLEAN: ('True'|'False');


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

//STRING : '"' (Letter+|Digit+ | ESCAPE|('\'"'))* '"' {self.text = self.text[1:-1]};
STRING :'"' ( '\\' [btnfr\\'] | ~[\b\t\f\r\n\\"'] | [']["] )* '"'{self.text = self.text[1:-1]};




UNCLOSE_STRING: '"' ( '\\' [btnfr\\'] | ~[\b\t\f\r\n\\"'] | [']["] )* {self.text = self.text[1:]};


ILLEGAL_ESCAPE:'"'(('\\'[btnfr\\'])|'\'"'|~[\\"])*('\\'~[bnftr'\\])
{   self.text=self.text[1:]
};
fragment Digit: [0-9];
fragment Letter:[a-zA-Z];


UNTERMINATED_COMMENT: '**'('*'?(~[*])+)*;
ERROR_CHAR:.;
 // skip spaces, tabs, newliness
