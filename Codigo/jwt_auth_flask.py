from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'

# Ruta para autenticación y generación del token
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    password = datos.get('password')

    if usuario == 'admin' and password == 'secret':
        token = jwt.encode({
            'usuario': usuario,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})

    return jsonify({'mensaje': 'Credenciales inválidas'}), 401

# Ruta protegida
@app.route('/api/protegida', methods=['GET'])
def protegida():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'mensaje': 'Token requerido'}), 401

    try:
        token = token.replace("Bearer ", "")
        datos = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'mensaje': f"Acceso concedido a {datos['usuario']}!"})
    except jwt.ExpiredSignatureError:
        return jsonify({'mensaje': 'Token expirado'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'mensaje': 'Token inválido'}), 401

if __name__ == '__main__':
    app.run(port=5000)
