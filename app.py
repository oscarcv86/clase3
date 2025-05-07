from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Dani')
def dani():
    return render_template('dani.html', numeros=range(1, 101))
#primer cambio
@app.route('/Taty')
def taty():
    return render_template('taty.html')

@app.route('/Oscar')
def oscar():
    return render_template('oscar.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        saludo = f"¡Hola {nombre} {apellido1} {apellido2}!"
        return render_template('formulario.html', saludo=saludo)
    return render_template('formulario.html', saludo=None)

if __name__ == '__main__':
    app.run(debug=True)