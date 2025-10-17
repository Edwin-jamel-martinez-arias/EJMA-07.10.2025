from flask import Flask, render_template

app = Flask(__name__)

autor = "Edwin Jamel Martínez Arias"


@app.route('/')
def inicio():
    return render_template('base.html', autor=autor)

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

if __name__ == '__main__':

    app.run(debug=True)
