from fastapi import FastAPI, Header, Request, HTTPException, status, Depends, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, Field
from typing import Optional
from jose import JWTError, jwt
import time

app = FastAPI(title="API Unificada de Seguridad", description="Ejemplo de API con múltiples métodos de autenticación", version="1.0.0")

# API Key
API_KEY = "123456"

# JWT
SECRET_KEY = "secret"  # Para ejemplo solamente
ALGORITHM = "HS256"

def crear_jwt(usuario: str):
    datos = {"sub": usuario, "exp": time.time() + 3600}
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

def verificar_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

# OAuth Simulado
clientes_validos = {"cliente1": "secreto1"}

@app.post("/oauth/token", summary="Simula entrega de token OAuth")
def obtener_token_oauth(client_id: str = Form(...), client_secret: str = Form(...)):
    if clientes_validos.get(client_id) != client_secret:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = crear_jwt(client_id)
    return {"access_token": token, "token_type": "bearer"}

# Modelos
class Item(BaseModel):
    nombre: str = Field(..., example="producto1")
    precio: float = Field(..., example=199.99)

# Seguridad HTTP Básica
security = HTTPBasic()

@app.get("/auth/basica", summary="Protegido con Autenticación Básica")
def auth_basica(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": f"Acceso básico permitido a {credentials.username}"}

# Endpoints
@app.get("/protegido/apikey", summary="Protegido con API Key")
def protegido_apikey(x_api_key: Optional[str] = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return {"mensaje": "Acceso con API Key permitido"}

@app.get("/protegido/ip", summary="Protegido por IP")
def protegido_ip(request: Request):
    ip_cliente = request.client.host
    if ip_cliente != "192.168.0.162":
        raise HTTPException(status_code=403, detail=f"Acceso denegado desde {ip_cliente}")
    return {"mensaje": f"Acceso permitido desde {ip_cliente}"}

@app.post("/protegido/jwt", summary="Protegido con JWT")
def protegido_jwt(token: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    payload = verificar_jwt(token.credentials)
    return {"mensaje": f"Token válido para {payload['sub']}"}

@app.post("/nuevo/item", summary="Crea un nuevo item validado")
def crear_item(item: Item):
    return {"mensaje": "Item creado", "item": item}

@app.get("/error", summary="Manejo de errores")
def error_demo():
    raise HTTPException(status_code=418, detail="Este es un error de prueba")
