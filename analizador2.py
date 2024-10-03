import ply.yacc as yacc
from tarealex import tokens, lexico  # Asegúrate de que los tokens estén correctamente importados

# Reglas para el analizador sintáctico
def p_statement_for_int(p):
    '''statement : PR'''
    if p[1].lower() == 'int':
        p[0] = ('int', 'Correcto')
    elif p[1].lower() == 'for':
        p[0] = ('for', 'Correcto')

def p_statement_pi(p):
    '''statement : PI'''
    p[0] = ('(', 'PI')

def p_statement_pd(p):
    '''statement : PD'''
    p[0] = (')', 'PD')

def p_statement_lli(p):
    '''statement : LLI'''
    p[0] = ('{', 'LLI')

def p_statement_lld(p):
    '''statement : LLD'''
    p[0] = ('}', 'LLD')

def p_statement_pc(p):
    '''statement : PC'''
    p[0] = (';', 'PC')   

def p_statement_hola_mundo(p):
    '''statement : ID'''
    if p[1].lower() == 'hola' or p[1].lower() == 'mundo':  # .lower() para manejar mayúsculas y minúsculas
        p[0] = (p[1], 'ID')  # Aquí asignamos "ID" cuando es "HOLA" o "MUNDO"
    elif p[1].lower() == 'x':
        p[0] = (p[1], 'ID')
    else:
        p[0] = (p[1], 'Incorrecto')  # Para cualquier otro identificador

# Regla para manejar errores de sintaxis
def p_error(p):
    print(f"Error de sintaxis en: {p.value if p else 'EOF'}")

# Crear el parser
parser = yacc.yacc()

# Función para realizar el análisis sintáctico
def analizar_sintaxis(entrada):
    resultado = []
    try:
        # Usamos el análisis léxico de 'lexico'
        tokens = lexico(entrada)
        parser.parse(entrada)  # Aquí se realiza el análisis sintáctico

        for token in tokens:
            if token['valor'].lower() == 'for' or token['valor'].lower() == 'int' or token['valor'].lower() == 'main':
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': 'Correcto'})
            elif token['valor'].lower() == 'hola' or token['valor'].lower() == 'mundo':
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': 'ID'})
            elif token['valor'].lower() == 'x':
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': f"{token['valor']} es un ID"})
            elif token['valor'] in ['(', ')', '{', '}', ';']:
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': token['tipo']})
            else:
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': 'Incorrecto'})
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        resultado.append({'linea': '-', 'tipo': '-', 'escritura': 'Error de sintaxis'})
    
    return resultado















