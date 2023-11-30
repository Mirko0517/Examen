from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculocompras', methods=['POST', 'GET'])
def calculocompras():
    nombre = request.form.get('nombre')
    edad_str = request.form.get('edad')
    cantidad_str = request.form.get('cantidad')

    if edad_str is None or cantidad_str is None:
        return render_template('calculocompras.html', mensaje_error="Ingrese la edad y la cantidad.")

    edad = int(edad_str)
    cantidad = int(cantidad_str)
    total = cantidad * 9000

    descuento = 0
    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25

    total_con_descuento = total - (total * descuento)

    return render_template('calculocompras.html', nombre=nombre, total=total, descuento=descuento, total_con_descuento=total_con_descuento)




@app.route('/iniciosesion', methods=['POST', 'GET'])
def iniciosesion():
    usuario = request.form.get('usuario')
    contrasena = request.form.get('contrasena')
    if usuario == 'juan' and contrasena == 'admin':
        return render_template('iniciosesion.html', mensaje='Bienvenido administrador Juan')
    elif usuario == 'pepe' and contrasena == 'user':
        return render_template('iniciosesion.html', mensaje='Bienvenido Usuario Pepe')
    else:
        return render_template('iniciosesion.html', mensaje='Usuario o contraseña incorrectos')


if __name__ == '__main__':
    app.run(debug=True)
