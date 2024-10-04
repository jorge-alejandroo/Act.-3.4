import ply.lex as lex

# Lista de tokens
tokens = (
    'ID',
    'PR',
    'VBL',
    'PC',   # Punto y coma
    'CMA',  # Coma
    'LLI',  # Llave izquierda
    'LLD',  # Llave derecha
    'PI',   # Paréntesis izquierdo
    'PD',   # Paréntesis derecho
    'CM',   # Comillas
)

# Lista de palabras reservadas y variables específicas
reserved = {
    'programa': 'PR',
    'int': 'PR',
    'read': 'PR',
    'printf': 'PR',
    'end': 'PR',
    'suma': 'ID', 
    'a': 'VBL',
    'b': 'VBL',
    'c': 'VBL',
}

def t_PR(t):
    r'programa|int|read|printf|end'
    return t

def t_ID(t):
    r'suma|[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores
    t.type = reserved.get(t.value, 'ID')  # Verifica si es reservada o ID
    return t

def t_VBL(t):
    r'a|b|c'
    return t

def t_PC(t):
    r';'
    return t

def t_CMA(t):
    r','
    return t

def t_LLI(t):
    r'\{'
    return t

def t_LLD(t):
    r'\}'
    return t

def t_PI(t):
    r'\('
    return t

def t_PD(t):
    r'\)'
    return t

def t_CM(t):
    r'\"'
    return t

# Manejo de saltos de línea para contar las líneas del código
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Crear el analizador léxico
def create_lexer():
    return lex.lex()

# Función de análisis léxico con contadores
def lexico(text):
    lexer = create_lexer()
    lexer.input(text)
    
    # Inicialización de contadores
    counters = {
        'PR': 0, 'ID': 0, 'VBL': 0, 'PC': 0, 'CMA': 0, 'LLI': 0,
        'LLD': 0, 'PI': 0, 'PD': 0, 'CM': 0
    }
    
    lexemes = []

    # Procesar cada token en el texto
    for tok in lexer:
        # Aumentar el contador según el tipo de token
        if tok.type in counters:
            counters[tok.type] += 1

        lexeme = {
            'linea': tok.lineno,
            'valor': tok.value,
            'PR': 'x' if tok.type == 'PR' else '',  # En lugar del tipo real, enviamos 'x'
            'ID': 'x' if tok.type == 'ID' else '',  # Identificador
            'VBL': 'x' if tok.type == 'VBL' else '',  # Variable
            'PC': 'x' if tok.type == 'PC' else '',  # Punto y coma
            'LLI': 'x' if tok.type == 'LLI' else '',  # Llave izquierda
            'LLD': 'x' if tok.type == 'LLD' else '',  # Llave derecha
            'PI': 'x' if tok.type == 'PI' else '',  # Paréntesis izquierdo
            'PD': 'x' if tok.type == 'PD' else '',  # Paréntesis derecho
            'CM': 'x' if tok.type == 'CM' else '',  # Coma
            'CMA': 'x' if tok.type == 'CMA' else '',
        }
        lexemes.append(lexeme)

    # Retorna los lexemas y los contadores
    return lexemes, counters

