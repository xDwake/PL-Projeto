import ply.lex as lex

tokens = [
    'ZOFFSETDATETIME',
    'OFFSETDATETIME',
    'DATETIME',
    'INTNUM',
    'EQUALS',
    'HEXNUM',
    'OCTNUM',
    'BINNUM',
    'BASICSTRING',
    'LITERALSTRING',
    'COMMENT',
    'PAR_RET_OPEN',
    'PAR_RET_CLOSE',
    'DATE',
    'TIME',
    'WORD',
    'DOT',
    'COMMA',
    'EMPTYLINE',
    'EXPONENCIALNUM',
    'SUBTITLE',
    'NEWLINE',
]

t_COMMENT = r'\#.*'
t_EQUALS = r'\='
t_PAR_RET_OPEN = r'\['
t_PAR_RET_CLOSE = r'\]'
t_DOT = r'\.'
t_COMMA = r'\,'
t_EMPTYLINE = r'^[ \t]*\n$'
t_NEWLINE = r'\n'

def t_OFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}[-+]\d{1}\:\d{2}'
    return t

def t_ZOFFSETDATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}Z'
    return t
    
def t_DATETIME(t):
    r'\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}'
    return t

def t_TIME(t):
    r"\d{2}\:\d{2}\:\d{2}"
    return t

def t_DATE(t):
    r'\d{4}\-\d{2}\-\d{2}'
    return t

def t_SUBTITLE(t):
    r'\.\w+'
    return t

def t_EXPONENCIALNUM(t):
    r"-*\d+[\.\d]*e\d+"
    return t
    
def t_WORD(t):
    r"[a-zA-Z\_]+"
    return t

def t_HEXNUM(t):
    r"0x[\d|a-f]+"
    return t

def t_BINNUM(t):
    r"0b[0|1]+"
    return t

def t_OCTNUM(t):
    r"0o[\d|\w]+"
    return t

def t_INTNUM(t):
    r"[-+]?[0-9]+"
    t.value = int(t.value)
    return t

def t_FLOATNUM(t):
    r"-*\d+\.\d+"
    t.value = float(t.value)
    return t

def t_BASICSTRING(t):
    r"\s?\"[\w|\-|\.|\s]+\""
    return t

def t_LITERALSTRING(t):
    r"\s?\'[\w|\-|\.|\s]+\'"
    return t

def t_error(t):
    print(f"Caracter ilegal {t.value}")
    t.lexer.skip(1)

t_ignore = ' \t'

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
with open('teste_multisubclasses.toml', 'r') as f:
    tab_in = f.read().replace('\n','')
    
lexer.input(tab_in)

while tok := lexer.token():
    print(tok)