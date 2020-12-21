// Nguyen Hoang Nam 1612115
grammar MP;

@lexer::header {
from lexererr import *
}
/*
@lexer::members{
def emit(self):
    result = super().emit()
    if self.type == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:-1])
    elif self.type == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif self.type == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}
*/

options{
	language=Python3;
}

program
	: many_declarations EOF
	;

many_declarations
	: declarations+
	;

declarations
	: variable_declarations | function_declarations | procedure_declarations
	;

variable_declarations
	: VAR list_var_declarations
	;

list_var_declarations
	: (var_declarations SEMICOLON)+
	;

var_declarations
	: IDENTIFIERS (COMMA IDENTIFIERS)* COLON mptype
	;

mptype
	: primitive_type | array_type
	;

primitive_type
	: INTEGER | BOOLEAN | STRING | REAL
	;

array_type
	: ARRAY LEFTSQUAREBRACKET lowerupper DOUBLEDOT lowerupper RIGHTSQUAREBRACKET OF primitive_type
	;

lowerupper
	: SUB_OP? INTEGERLITERAL
	;

function_declarations
	: FUNCTION IDENTIFIERS LEFTBRACKET param_list? RIGHTBRACKET COLON mptype SEMICOLON variable_declarations? compound_statement
	;

param_list
	: var_declarations (SEMICOLON var_declarations)*
	;

procedure_declarations
	: PROCEDURE IDENTIFIERS LEFTBRACKET param_list? RIGHTBRACKET SEMICOLON variable_declarations? compound_statement
	;

expression
	: exp1
	;

exp1
	: exp1 AND THEN exp2
	| exp1 OR ELSE exp2
	| exp2
	;

exp2
	: exp3 E_OP exp3
	| exp3 NE_OP exp3
	| exp3 L_OP exp3
	| exp3 LE_OP exp3
	| exp3 G_OP exp3
	| exp3 GE_OP exp3
	| exp3
	;

exp3
	: exp3 ADD_OP exp4
	| exp3 SUB_OP exp4
	| exp3 OR exp4
	| exp4
	;

exp4
	: exp4 DIV_OP exp5
	| exp4 MUL_OP exp5
	| exp4 DIV exp5
	| exp4 MOD exp5
	| exp4 AND exp5
	| exp5
	;

exp5
	: SUB_OP exp5
	| NOT exp5
	| exp6
	;
exp6
	: exp7 (LEFTSQUAREBRACKET exp1 RIGHTSQUAREBRACKET)?
	;

exp7
	: LEFTBRACKET exp1 RIGHTBRACKET
	| exp8
	;

exp8
	: operands
	;

operands
	: literal | IDENTIFIERS | funccall
	;

index_expression
	: expression LEFTSQUAREBRACKET expression RIGHTSQUAREBRACKET
	;

funccall
    : IDENTIFIERS LEFTBRACKET (expression (COMMA expression)*)? RIGHTBRACKET
    ;

literal
    : STRINGLITERAL | INTEGERLITERAL | REALLITERAL | BOOLEANLITERAL
    ;

statement
	: assignment_statement
	| if_statement
	| for_statement
	| while_statement
	| break_statement
	| continue_statement
	| return_statement
	| call_statement
	| compound_statement
	| with_statement
	;

assignment_statement
    : ((iid | index_expression) ASSIGN_OP)+  expression SEMICOLON
    ;

iid
	: IDENTIFIERS
	;

if_statement
    : IF expression THEN statement (ELSE statement)?
    ;

while_statement
    : WHILE expression DO statement
    ;

for_statement
    : FOR IDENTIFIERS ASSIGN_OP expression (TO|DOWNTO) expression DO statement
    ;

break_statement
    : BREAK SEMICOLON
    ;

continue_statement
    : CONTINUE SEMICOLON
    ;

return_statement
    : RETURN expression? SEMICOLON
    ;

compound_statement
    : BEGIN statement* END
    ;

with_statement
    : WITH list_var_declarations DO statement
    ;

call_statement
    : funccall SEMICOLON
    ;


// keywords
WITH
    : W I T H
    ;

BREAK
	: B R E A K
	;

CONTINUE
	: C O N T I N U E
	;

FOR
	: F O R
	;

TO
	: T O
	;

DOWNTO
	: D O W N T O
	;

DO
	: D O
	;

IF
	: I F
	;

THEN
	: T H E N
	;

ELSE
	: E L S E
	;

RETURN
	: R E T U R N
	;

WHILE
	: W H I L E
	;

BEGIN
	: B E G I N
	;

END
	: E N D
	;

FUNCTION
	: F U N C T I O N
	;

PROCEDURE
	: P R O C E D U R E
	;

VAR
	: V A R
	;

fragment TRUE
	: T R U E
	;

fragment FALSE
	: F A L S E
	;

ARRAY
	: A R R A Y
	;

OF
	: O F
	;

REAL
	: R E A L
	;

BOOLEAN
	: B O O L E A N
	;

INTEGER
	: I N T E G E R
	;

STRING
	: S T R I N G
	;

NOR
	: N O R
	;

AND
	: A N D
	;

OR
	: O R
	;

DIV
	: D I V
	;

MOD
	: M O D
	;

NOT
	: N O T
	;


// 3.1
// skip spaces, tabs, newlines
WS
	: [ \t\r\n\f]+	-> skip
	;

// 3.2
// skip comment
BLOCK_COMMENT1
    : '(*' .*? '*)'	-> skip
	;

BLOCK_COMMENT2
	: '{' .*? '}' 	-> skip
	;

LINE_COMMENT
    : '//' ~[\r\n\f]*	-> skip
	;

BOOLEANLITERAL
	: TRUE | FALSE
	;

// 3.3

// identifiers
IDENTIFIERS:
	(LETTER | UNDERSCORE) (LETTER | UNDERSCORE | DIGIT)*
	;
// Operators
ADD_OP
	: '+'
	;

SUB_OP
	: '-'
	;

MUL_OP
	: '*'
	;

DIV_OP
	: '/'
	;

NE_OP
	: '<>'
	;

E_OP
	: '='
	;

L_OP
	: '<'
	;

LE_OP
	: '<='
	;

G_OP
	: '>'
	;

GE_OP
	: '>='
	;

ASSIGN_OP
	: ':='
	;

// 3.4
// Separators
LEFTSQUAREBRACKET
	: '['
	;

RIGHTSQUAREBRACKET
	: ']'
	;

COLON
	: ':'
	;

LEFTBRACKET
	: '('
	;

RIGHTBRACKET
	: ')'
	;

SEMICOLON
	: ';'
	;

DOUBLEDOT
	: '..'
	;

COMMA
	: ','
	;

// 3.5
// Literal definition
INTEGERLITERAL
	: DIGIT+
	;

REALLITERAL
	: ((DIGIT+ ('.' DIGIT*)?) | ('.' DIGIT+))  EXPONENT?
	;


STRINGLITERAL
	: '"' ( '\\' [bfnrt'"\\] | ~[\b\f\n\r\t'"\\] )* '"'
	{self.text = self.text[1:-1]}
	;

// Fragments define
fragment UNDERSCORE
	: '_'
	;

fragment LETTER
	: 'a'..'z' | 'A'..'Z'
	;

fragment DIGIT
	: '0'..'9'
	;

fragment EXPONENT
	: E (ADD_OP | SUB_OP)? DIGIT+
	;

// Characters
fragment A
	: ('a' | 'A')
	;

fragment B
	: ('b' | 'B')
	;

fragment C
	: ('c' | 'C')
	;

fragment D
	: ('d' | 'D')
	;

fragment E
	: ('e' | 'E')
	;

fragment F
	: ('f' | 'F')
	;

fragment G
	: ('g' | 'G')
	;

fragment H
	: ('h' | 'H')
	;

fragment I
	: ('i' | 'I')
	;

fragment J
	: ('j' | 'J')
	;

fragment K
	: ('k' | 'K')
	;

fragment L
	: ('l' | 'L')
	;

fragment M
	: ('m' | 'M')
	;

fragment N
	: ('n' | 'N')
	;

fragment O
	: ('o' | 'O')
	;

fragment P
	: ('p' | 'P')
	;

fragment Q
	: ('q' | 'Q')
	;

fragment R
	: ('r' | 'R')
	;

fragment S
	: ('s' | 'S')
	;

fragment T
	: ('t' | 'T')
	;

fragment U
	: ('u' | 'U')
	;

fragment V
	: ('v' | 'V')
	;

fragment W
	: ('w' | 'W')
	;

fragment X
	: ('x' | 'X')
	;

fragment Y
	: ('y' | 'Y')
	;

fragment Z
	: ('z' | 'Z')
	;

ILLEGAL_ESCAPE
	: '"' ( '\\' [bfnrt"'\\] | ~[\b\f\n\r\t"'\\] )* ('\\' ~[bfnrt"'\\] | [\b\f\t"'\\])
	{raise IllegalEscape(self.text[1:])}
	;
//'
UNCLOSE_STRING
	: '"' ( '\\' [bfnrt"'\\] | ~[\b\f\n\r\t"'\\] )*
	{raise UncloseString(self.text[1:])}
	;

ERROR_CHAR
	: .
	{raise ErrorToken(self.text)}
	;