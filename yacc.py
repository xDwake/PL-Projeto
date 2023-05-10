import ply.yacc as yacc

from lexer import tokens
num_indents = 0
string = ""

def close_classe():
    global num_indents
    global string
    string = ""
    while num_indents > 0:
        string += "\t" * num_indents + '}' + '\n'
        num_indents -=1
    string = string[:-1]

def p_programa(p):
    'programa : title conteudo'
    p[0] = '{' + '\n' +  p[1] + ',\n' + p[2] +'\n' + '}'

def p_conteudo(p):
    '''conteudo : conteudo classe
                | classe'''
    if len(p) == 2:
        p[0] = p[1]
    
    else:
        p[0] = p[1] + ',' + '\n' + p[2]
    

def p_classe(p):
    'classe : headers linhas'
    global string
    close_classe()
    p[0] = p[1]  + '\n' + p[2] + '\n' + string

def p_headers(p):
    
    '''headers : headers header
                | header'''
    global num_indents
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[2]
    num_indents +=1
    
def p_header(p):
    '''header : PAR_RET_OPEN WORD PAR_RET_CLOSE
                | PAR_RET_OPEN WORD DOT WORD PAR_RET_CLOSE'''

    if len(p) == 4:
        p[0] = '\t' * (num_indents+1) + '"' + p[2] + '"' + ': ' + '{'
    else:
        p[0] = '\t' * (num_indents+1) + '"' + p[4] + '"' + ': ' + '{'

def p_linhas(p):
    '''linhas : linhas linha
             | linha'''
    global num_indents
    if len(p) == 2:
        p[0] = '\t' * (num_indents) + p[1]
    else:
        p[0] = p[1] + ',' + '\n' + '\t'* (num_indents) + p[2]
    
def p_title(p):
    'title : linha'
    p[0] = p[1]

def p_linha(p): 
    '''linha : key EQUALS valor
            | comentario'''

    if len(p) == 2: 
        pass
    else:
        p[0] = '\t' + '"' + p[1] + '"' + ': ' + p[3] 

def p_comentario(p):
    'comentario : COMMENT'
    pass

def p_key(p): 
    'key : WORD'
    p[0] = p[1]

def p_valor(p):
    '''valor : BASIC_STRING
            '''

    p[0] = p[1]


def p_error(p):
    print("ERRO SINTATICO")

parser = yacc.yacc()
tab_in = ''' title = "baguete"
[owner]
name = "Tom Preston-Werner"
dob = "ashfahr"
dobas = "aufasfha"
dobassss = "aufasfha"

[database]
[database.coiso]
enabled = "true"
ports = "coiso"
data = "delta"
temp_targets = "pefomance"
'''
with open("teste.json",'w') as f: 
    f.write(parser.parse(tab_in,debug=True))
    