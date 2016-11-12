#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

paises = [
    {
        'nombre': 'brazil',
        'codigo': u'55',
    },
    {
        'nombre': 'france',
        'codigo': u'33',
    },
    {
        'nombre': 'italy',
        'codigo': u'39',
    },
    {
        'nombre': 'japan',
        'codigo': u'81',
    },
]


@app.route("/")
def home():
    return """
    <html>
    <body> 
        <h2>Bienvenido a la página principal de la API de Prefijos telefónicos mundiales:</h2>
        <h4>Uso:</h4>
        <h5>Mostrar todos los paises:</h5>
        <p>/api/paises<p>
        <h5>Mostrar un pais:</h5>
        <p>/api/paises/"pais"</p>
        <p>Ej: /api/paises/france</p>
    </body> 
</html> """ 


def listar_paises(pais):
    nuevo_pais = {}
    for campo in pais:
        if campo == 'nombre':
            nuevo_pais['uri'] = url_for('get_pais', nombre_pais = pais['nombre'], _external = True)
        else:
            nuevo_pais[campo] = pais[campo]
    return nuevo_pais
    
@app.route('/api/paises', methods = ['GET'])
def get_paises():
    return jsonify( { 'paises': map(listar_paises, paises) } )

@app.route('/api/paises/<nombre_pais>', methods = ['GET'])
def get_pais(nombre_pais):
    pais = filter(lambda p: p['nombre'] == nombre_pais, paises)
    if len(pais) == 0:
        abort(404)
    return jsonify( { 'pais': listar_paises(pais[0]) } )

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

