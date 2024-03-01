from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Datos personales
datos_personales = {
    'nombre': 'Eduardo Medina',
    'carrera': 'Ingeniería en Sistemas y Electrónica',
}

@app.route('/')
def index():

    return render_template('index.html', datos=datos_personales)

@app.route('/Mishabilidades')
def Mishabilidades():

    return render_template('Mishabilidades.html')


@app.route('/Misdatos')
def Misdatos():

    return render_template('Misdatos.html')

@app.route('/comentarios', methods=['GET'])
def mostrar_comentarios():
    # Leer comentarios desde el archivo
    with open('comentarios.txt', 'r') as file:
        comentarios = file.readlines()
    return render_template('comentarios.html', comentarios=comentarios)

# Ruta para guardar el comentario
@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    nombre = request.form['nombre']
    comentario = request.form['comentario']
    nuevo_comentario = f'{nombre}: {comentario}\n'

    # Agregar el nuevo comentario al archivo de texto
    with open('comentarios.txt', 'a') as file:
        file.write(nuevo_comentario)

    return redirect('/comentarios')


if __name__ == '__main__':
    app.run(debug=True)
