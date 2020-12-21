grammar BKIT;
program  : (var_declare|func_declare)* EOF;



//Tokens indentify sections
//ID section

//Fragment for ID


//Keyword section
INT: 'int';
FLOAT: 'float';
RETURN: 'return';

fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment UNDERSCORE: '_';
fragment NUMBER: [0-9];

ID: (LOWERCASE|UPPERCASE|UNDERSCORE)(LOWERCASE|UPPERCASE|UNDERSCORE|NUMBER)*;

//Literal section
INTLIT: [1-9][0-9]* | '0';
FLOATLIT: INTLIT([.][0-9]+)?([eE][+-]?[0-9]+)?;


//Seperators section
LP: '(';    //Left parenthesis
RP: ')';    //Right parenthesis
LB: '{';    //Left brace
RB: '}';    //Right brace
CM: ',';    //Comma
SM: ';';    //Semi-colon

//Expression section
EQ: '=';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

func_declare: type_var ID LP (type_var list_id (SM type_var list_id)* )? RP LB body RB;
list_id: ID (CM ID)*;
body: (var_declare | assign_stmt | call_stmt | return_stmt)*;

var_declare: type_var list_id SM;
type_var: INT|FLOAT;

assign_stmt: ID EQ exp SM;
call_stmt: func_call SM;
return_stmt: RETURN exp SM;

exp: operands
    | exp (MUL | DIV ) exp
    | operands SUB operands
    | exp ADD exp
    ;
operands : (LP exp RP) | func_call | ID | INTLIT | FLOATLIT;
func_call: ID LP (exp (CM exp)*)? RP;


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;