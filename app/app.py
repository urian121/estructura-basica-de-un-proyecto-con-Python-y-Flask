from flask import Flask, request, redirect, render_template, url_for


# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'


@app.route('/')
def inicio():
    return render_template('base_index.html')


@app.route('/info', methods=['GET'])
def info():
    return render_template('public/pages/info.html')


@app.route('/perfil', methods=['GET'])
def perfil():
    return render_template('public/pages/perfil.html')

# Redireccionando cuando la página no existe


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))


@app.errorhandler(500)
def server_error(error):
    return redirect(url_for('inicio'))


# Ejecutando el objeto Flask
if __name__ == '__main__':
    app.run(debug=True, port=5600)
