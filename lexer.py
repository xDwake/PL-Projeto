import ply.lex as lex

tokens = [
    'INTNUM',
    'EQUALS',
    'HEXNUM',
    'OCTNUM',
    'BINNUM',
    'BASIC_STRING',
    'LITERAL_STRING',
    'COMMENT',
    'PAR_RET_OPEN',
    'PAR_RET_CLOSE',
    'DATE',
    'TIME',
    'WORD',
    'DOT',
    'COMMA'
]

t_COMMENT = r'\#.*'
t_EQUALS = r'\='
t_PAR_RET_OPEN = r'\['
t_PAR_RET_CLOSE = r'\]'
t_DOT = r'\.'
t_COMMA = r'\,'

def t_DATE(t):
    r"\d{4}-\d{2}-\d{2}"
    return t

def t_TIME(t):
    r"\d{2}:\d{2}:\d{2}"
    return t

def t_WORD(t):
    r"[a-zA-Z\_]+"
    return t

def t_HEXNUM(t):
    r"0x\w+"
    return t

def t_BINNUM(t):
    r"0b\w+"
    return t

def t_OCTNUM(t):
    r"0o\w+"
    return t

def t_INTNUM(t):
    r"[-|+]*\d+"
    t.value = int(t.value)
    return t

def t_FLOATNUM(t):
    r"-*\d+\.\d+"
    t.value = float(t.value)
    return t

def t_BASIC_STRING(t):
    r"\s?\"[\w|\-|\.|\s]+\""
    return t

def t_LINEAR_STRING(t):
    r"\s?\'[\w|\-|\.|\s]+\'"
    return t

def t_error(t):
    print(f"Caracter ilegal {t.value}")
    t.lexer.skip(1)

t_ignore = ' \n\t'

lexer = lex.lex()


string = """
title = "TOML Example"
[owner]
name = "Tom Preston-Werner"
date = 2010-04-23
time = 21:30:00
[database]
server = "192.168.1.1"
ports = [ 8001, 8001, 8002 ]
connection_max = 5000
enabled = true
[servers]
[servers.alpha]
ip = "10.0.0.1"
dc = "eqdc10"
[servers.beta]
ip = "10.0.0.2"
dc = "eqdc10"
# Line breaks are OK when inside arrays
hosts = [
"alpha",
"omega"
]
"""

lexer.input(string)
while tok := lexer.token():
    print(tok)