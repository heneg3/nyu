from ply import yacc

from scanner import scanner
from parser.ast import Node


tokens = scanner.tokens

precedence = (
    ('right', 'uminus'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'ASSIGN'),
)


def p_program(p):
    '''
    program : function_def program
            | decl program
            | function_decl program
            | empty
    '''
    pass

def p_decl(p):
    '''
    decl : kind var_list SEMI
    '''
    pass

def p_kind(p):
    '''
    kind : int_kw
         | float_kw
    '''
    pass

def p_var_list(p):
    '''
    var_list : identifier var_list_prime
    '''
    pass

def p_var_list_prime(p):
    '''
    var_list_prime : COMMA var_list
                   | empty
    '''
    pass

def p_function_decl(p):
    '''
    function_decl : kind identifier LPAR kind RPAR SEMI
    '''
    pass

def p_function_def(p):
    '''
    function_def : kind identifier LPAR kind identifier RPAR body
    '''
    pass

def p_body(p):
    '''
    body : LBRACE body_prime RBRACE
    '''
    pass

def p_body_prime(p):
    '''
    body_prime : decl body_prime
               | stmt body_prime
               | empty
    '''
    pass

def p_stmt(p):
    '''
    stmt : expr SEMI
         | if_kw LPAR bool_expr RPAR stmt else_stmt
         | while_kw LPAR bool_expr RPAR stmt
         | read_kw var_list SEMI
         | write_kw write_expr_list SEMI
         | return_kw expr SEMI
    '''
    pass

def p_else_stmt(p):
    '''
    else_stmt : else_kw stmt
              | empty
    '''
    pass

def p_write_expr_list(p):
    '''
    write_expr_list : expr write_expr_list_prime
                    | string write_expr_list_prime
    '''
    pass

def p_write_expr_list_prime(p):
    '''
    write_expr_list_prime : COMMA write_expr_list
                          | empty
    '''
    pass

def p_factor(p):
    '''
    factor : identifier
           | integer_literal
           | float_literal
           | function_call
           | LPAR expr RPAR
    '''
    pass

def p_bool_expr(p):
    '''
    bool_expr : expr boolop expr
    '''
    pass

def p_function_call(p):
    '''
    function_call : identifier LPAR expr RPAR
    '''
    pass

def p_term(p):
    '''
    term : uminus factor term
         | mulop uminus factor
         | empty
    '''
    pass

def p_uminus(p):
    '''
    uminus : MINUS %prec uminus
           | empty
    '''
    pass

def p_mulop(p):
    '''
    mulop : MULTIPLY
          | DIVIDE
    '''
    pass

def p_expr1(p):
    '''
    expr1 : term expr1_prime
    '''
    pass

def p_expr1_prime(p):
    '''
    expr1_prime : addop expr1
                | empty
    '''
    pass

def p_addop(p):
    '''
    addop : PLUS
          | MINUS
    '''
    pass

def p_boolop(p):
    '''
    boolop : LT
           | GT
           | EQUAL
           | LE
           | GE
    '''
    pass

def p_expr(p):
    '''
    expr : identifier ASSIGN expr
         | expr1
    '''
    pass

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print(p)

parser = yacc.yacc()
