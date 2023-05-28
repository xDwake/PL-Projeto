import ply.yacc as yacc
from lexer import tokens, tab_in
import json


def p_program(p):
    'program : linha table'
    p[0] = p[1]
    p[0].update(p[2])

def p_table(p):
    '''table : table categoria
             | categoria'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].update(p[2])
    
def p_categoria(p):
    '''categoria : header conteudo
                 | header subtitle conteudo
                 | subtitle conteudo'''
    if len(p) == 3:
        p[0] = { p[1] : p[2]}
    else:
        p[0] = {p[1] : {p[2] : p[3]}}

def p_header(p):
    '''header : PAR_RET_OPEN WORD PAR_RET_CLOSE'''
    p[0] = p[2]
    
def p_subtitle(p):
    '''subtitle : PAR_RET_OPEN WORD SUBTITLE PAR_RET_CLOSE'''
    p[0] = p[3].strip('.')

def p_conteudo(p):
    '''conteudo : conteudo linha
                | linha'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].update(p[2])

def p_basicstring(p):
    '''basicstring : BASICSTRING'''
    p[0] = p[1].strip("\"")

def p_linha(p):
    '''linha : WORD EQUALS value
             | WORD EQUALS PAR_RET_OPEN lista PAR_RET_CLOSE'''
    if len(p) == 4:
        p[0] = {p[1] : p[3]}
    else:
        p[0] = {p[1] : p[4]}

def p_lista(p):
    '''lista : lista COMMA value
             | value'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_value(p):
    '''value : basicstring
             | LITERALSTRING
             | TIME
             | DATE
             | EXPONENCIALNUM
             | BINNUM
             | INTNUM
             | HEXNUM
             | OCTNUM
             | lista
             '''

    p[0] = p[1]

def p_error(p):
    print("ERRO SINTATICO")


parser = yacc.yacc()


result = parser.parse(tab_in,debug=True)
print(tab_in)

def convert_to_json(output):

    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    file.write("[\n")
    json.dump(result, file, indent= 3,separators=(',',': ')) 
    file.write("\n]")
    
    file.close()

convert_to_json("./saida")