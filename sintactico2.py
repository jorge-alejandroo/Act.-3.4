import ply.yacc as yacc
from lexico2 import tokens, lexico

# Reglas de la gramática para la sintaxis correcta
def p_program(p):
    '''program : PR ID PI PD LLI declarations statements end_reserved end_block'''
    pass

def p_declarations(p):
    '''declarations : PR variable_list PC'''
    pass

def p_variable_list(p):
    '''variable_list : VBL
                     | VBL CMA variable_list'''
    pass

# Modificar la regla de statements para verificar las sentencias necesarias
def p_statements(p):
    '''statements : read_statement read_statement assign_statement print_statement'''

    # Obtener las variables leídas de cada read_statement
    variable_1 = p[1][1]
    variable_2 = p[2][1]
    
    # Verificar si se leyeron las variables necesarias
    if variable_1 != 'a' or variable_2 != 'b':
        errores_sintacticos.append("Error: Falta la lectura de las variables 'a' y 'b'.")
    
    # Verificar que la asignación sea correcta
    asignacion = p[3]
    if asignacion[0] != 'c':  # Verificar que la asignación sea a 'c'
        errores_sintacticos.append("Error: La asignación debe ser a la variable 'c'.")
    
    if asignacion[1] != 'a' or asignacion[2] != 'b':  # Verificar que la suma sea entre 'a' y 'b'
        errores_sintacticos.append("Error: La suma debe involucrar las variables 'a' y 'b'.")

def p_read_statement(p):
    '''read_statement : PR VBL PC'''
    p[0] = ("Lectura correcta", p[2])  # Guardar la variable leída

def p_assign_statement(p):
    '''assign_statement : VBL '=' VBL '+' VBL PC'''
    p[0] = (p[1], p[3], p[5])  # Guardar la asignación ('c', 'a', 'b')

def p_print_statement(p):
    '''print_statement : PR PI CM ID CM PD'''
    pass

# Este es el penúltimo: bloque termina con una palabra reservada (por ejemplo, 'end')
def p_end_reserved(p):
    '''end_reserved : PR PC'''
    pass

# Este es el último: bloque termina con 'LLD' (llave derecha)
def p_end_block(p):
    '''end_block : LLD'''
    pass

# Manejo de errores sintácticos
def p_error(p):
    if p:
        error_msg = f"Error de sintaxis: {p.value}"
        errores_sintacticos.append(error_msg)
        # Imprimir el mensaje de error en consola
        print(error_msg)
    else:
        error_msg = "Error de sintaxis: Token inesperado"
        errores_sintacticos.append(error_msg)
        # Imprimir el mensaje de error en consola
        print(error_msg)

# Crear el parser
parser = yacc.yacc()

# --------- Análisis Sintáctico ---------
errores_sintacticos = []

def analizar_sintaxis(entrada):
    global errores_sintacticos
    errores_sintacticos = []  # Limpiar errores previos
    
    # Realizamos primero el análisis léxico y sintáctico
    parser.parse(entrada)
    
    # Si no se encontraron errores, devolver mensaje de éxito
    if not errores_sintacticos:
        return "Sintaxis Correcta"
    else:
        # Devolver los errores acumulados
        return "\n".join(errores_sintacticos)













