# API Segura - Entrega 1 y 2

Este repositorio contiene los archivos utilizados para las entregas del Trabajo Práctico Final de la materia **Desarrollo de Software Seguro**.

---

## 📌 Entrega 1 - Autenticación Básica

Se implementaron dos APIs simples con autenticación básica:

- **basic_auth_flask.py** → API en Flask protegida con usuario y contraseña.
- **basic_auth_fastapi.py** → API en FastAPI protegida con usuario y contraseña.

Ambas están documentadas con Swagger UI a través de OpenAPI, permitiendo su prueba desde el navegador.

---

## 📌 Entrega 2 - Autenticación Avanzada y Control de Acceso

Se agregaron nuevas implementaciones para proteger las APIs de forma más robusta:

- **ip_auth_flask.py** → Control de acceso por IP en Flask.
- **ip_auth_fastapi.py** → Control de acceso por IP en FastAPI.
- **jwt_auth_flask.py** → Autenticación con JWT (token firmado) en Flask.
- **swagger_jwt_flask.py** → JWT integrado con Swagger UI para pruebas desde el navegador.

---

## 🔒 Requisitos

- Python 3.8 o superior
- Instalar dependencias con:
  ```bash
  pip install flask fastapi uvicorn pyjwt

## Autor
Jorge Andrés Jaime
Estudiante de Tecnicatura Universitaria en Ciberseguridad - UGR
