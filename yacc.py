import ply.yacc as yacc
from lexer import tokens
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
    'categoria : header conteudo'

    p[0] = { p[1] : p[2] }

def p_header(p):
    '''header : PAR_RET_OPEN WORD PAR_RET_CLOSE'''
    p[0] = p[2]

def p_conteudo(p):
    '''conteudo : conteudo linha
                | linha'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].update(p[2])

def p_linha(p):
    '''linha : WORD EQUALS value '''
    p[0] = {p[1] : p[3]}

def p_basicstring(p):
    '''basicstring : BASIC_STRING'''
    p[0] = p[1].strip("\"")

def p_value(p):
    '''value : basicstring'''
    p[0] = p[1]

def p_error(p):
    print("ERRO SINTATICO")
parser = yacc.yacc()
tab_in = ''' title = "TOML"
[owner]
name = "Tom Preston-Werner"
dob = "ashfahr"
dobas = "aufasfha"
dobassss = "aufasfha"
[database]
enabled = "true"
ports = "coiso"
data = "delta"
'''

'''[database]
[database.coiso]
enabled = "true"
ports = "coiso"
data = "delta"
temp_targets = "pefomance"
[database.pescoso]
coiso = " batata frita"
[database.corno]
merda = "paistotudo"
'''
result = parser.parse(tab_in,debug=True)
print(result)
def convert_to_json(output):

    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    file.write("[\n")
    json.dump(result, file, indent= 3,separators=(',',': ')) 
    file.write("\n]")
    
    file.close()

convert_to_json("saida")