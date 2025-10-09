from flask import Flask, render_template

app = Flask(__name__)

# Variable autor
autor = "Edwin Jamel Martínez Arias"

# Página de inicio
@app.route('/')
def inicio():
    return render_template('index.html', autor=autor)

# Página de animales
@app.route('/animales')
def animales():
    return render_template('animales.html', autor=autor)

# Página de vehículos antiguos
@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html', autor=autor)

# Página de maravillas del mundo
@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', autor=autor)

# Página acerca de
@app.route('/acercade')
def acercade():
    return render_template('acercade.html', autor=autor)

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)