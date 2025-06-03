from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "clave-secreta"

@app.route('/api/protegida', methods=['GET'])
def ruta_protegida():
    clave = request.headers.get('X-API-Key')
    if clave != API_KEY:
        return jsonify({"mensaje": "API Key inválida"}), 403
    return jsonify({"mensaje": "Acceso autorizado por API Key"})

if __name__ == '__main__':
    app.run()

