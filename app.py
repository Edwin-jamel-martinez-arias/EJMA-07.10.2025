from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Necesario para que 'flash' funcione
app.secret_key = 'tu_clave_secreta_aqui' 

autor = "Edwin Jamel Martínez Arias"

@app.route('/')
def base():
    # Redirige la raíz al inicio
    return redirect(url_for('inicio')) 

@app.route('/inicio')
def inicio():
    return render_template('inicio.html', autor=autor)

@app.route('/animales')
def animales():
    return render_template('animales.html', autor=autor)

@app.route('/vehiculos')
def vehiculos():
    return render_template('carros.html', autor=autor)

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', autor=autor)

@app.route('/acercade')
def acercade():
    return render_template('acerca.html', autor=autor)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        dia = request.form.get('dia')
        mes = request.form.get('mes')
        anio = request.form.get('anio')
        genero = request.form.get('genero')
        email = request.form.get('email')
        clave = request.form.get('clave')
        confirmar_clave = request.form.get('confirmar_clave')

        if clave != confirmar_clave:
            flash('Error: Las contraseñas no coinciden.', 'error')
            return render_template('registro.html', autor=autor, request_form=request.form)
            
        flash('Registro exitoso!', 'success')
        return redirect(url_for('inicio'))

    return render_template('registro.html', autor=autor)

if __name__ == "__main__":
    app.run(debug=True)
