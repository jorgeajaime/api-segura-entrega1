from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps
from flasgger import Swagger, swag_from

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_para_jwt'

# ⚙️ Configuración de Swagger con soporte para Bearer token
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Autenticación JWT",
        "description": "API con protección JWT",
        "version": "1.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Ingrese el token JWT con el prefijo 'Bearer ', por ejemplo: Bearer eyJhbGci..."
        }
    },
    "security": [{"Bearer": []}]
}

swagger = Swagger(app, template=swagger_template)

# 🔒 Decorador para verificar el token
def token_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            return jsonify({'mensaje': 'Token faltante'}), 401
        try:
            datos = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401
        return f(usuario=datos['usuario'], *args, **kwargs)
    return decorador

# 🔐 Ruta para obtener el token
@app.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Autenticación JWT'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'usuario': {'type': 'string'},
                    'contraseña': {'type': 'string'}
                },
                'required': ['usuario', 'contraseña']
            }
        }
    ],
    'responses': {
        200: {'description': 'Token generado correctamente'},
        401: {'description': 'Credenciales inválidas'}
    }
})
def login():
    datos = request.get_json()
    if datos['usuario'] == 'admin' and datos['contraseña'] == 'secret':
        token = jwt.encode({
            'usuario': datos['usuario'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'mensaje': 'Credenciales inválidas'}), 401

# 🔒 Ruta protegida con JWT
@app.route('/api/protegida', methods=['GET'])
@swag_from({
    'tags': ['Autenticación JWT'],
    'security': [{'Bearer': []}],
    'responses': {
        200: {'description': 'Acceso concedido'},
        401: {'description': 'Token inválido o faltante'}
    }
})
@token_requerido
def api_protegida(usuario):
    return jsonify({'mensaje': f'Acceso concedido a {usuario}!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
