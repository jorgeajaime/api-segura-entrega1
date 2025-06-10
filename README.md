# API Segura - Entrega Final

Este proyecto demuestra una API REST desarrollada con **FastAPI**, incorporando múltiples métodos de autenticación. La documentación completa se genera automáticamente con **Swagger UI**.

## 🔐 Métodos de Autenticación Implementados

| Método    | Endpoint        | Descripción                                                                  |
|-----------|-----------------|------------------------------------------------------------------------------|
| API Key   | `/auth/apikey`  | Requiere enviar una API Key en el header `x-api-key`.                        |
| JWT       | `/auth/jwt`     | Requiere un token JWT válido en el header `Authorization`.                   |
| Por IP    | `/auth/ip`      | Solo permite el acceso desde una IP específica.                              |
| Básica    | `/auth/basica`  | Simulación de autenticación básica con usuario y contraseña en la URL.       |
| OAuth 2.0 | `/auth/token`   | Simula el flujo de autorización generando un JWT válido.                     |

## 🚀 Cómo ejecutar el proyecto

### 1. Cloná el repositorio:

```bash
git clone https://github.com/jorgeajaime/api-segura-entrega1.git
cd api-segura-entrega1/Codigo
```

### 2. Instalá las dependencias necesarias:

```bash
pip install fastapi uvicorn python-jose
```

### 3. Ejecutá el servidor:

```bash
uvicorn api_unificada:app --reload
```

``` 

---

**Archivo: requirements.txt**

```text
fastapi
uvicorn
python-jose
```

---

**Archivo: .gitignore**

```gitignore
venv/
__pycache__/
*.pyc
.env
.DS_Store


### 4. Accedé a la documentación interactiva:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📂 Estructura del proyecto

```
/Codigo
├── apiunificada.py         # API con todos los métodos de autenticación
├── OAuth.py                # Flujo simulado de OAuth
├── swagger_jwt_flask.py    # Implementación JWT con Flask
├── README.md               # Este archivo
```

## ✅ Datos de prueba

- **API Key**: `123456`
- **Credenciales OAuth**:
  - client_id: `cliente1`
  - client_secret: `secreto1`


## Autor
Jorge Andrés Jaime
Estudiante de Tecnicatura Universitaria en Ciberseguridad - UGR
