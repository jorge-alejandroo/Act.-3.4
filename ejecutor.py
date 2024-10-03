from flask import Flask, request, render_template
from lexico2 import lexico
from sintactico2 import analizar_sintaxis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('analizador3.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    if request.method == 'POST':
        codigo = request.form['text']  # Aquí estamos obteniendo el texto del formulario
        
        # Análisis léxico
        lexemes, counters = lexico(codigo)

        # Análisis sintáctico
        resultado_sintactico = analizar_sintaxis(codigo)
        
        # Renderizar el HTML con los resultados
        return render_template('analizador3.html', tokens=lexemes, sintaxis=resultado_sintactico, conteos=counters)

if __name__ == "__main__":
    app.run(debug=True)


