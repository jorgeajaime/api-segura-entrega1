from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

def verificar_credenciales(credenciales: HTTPBasicCredentials = Depends(security)):
    usuario_valido = credenciales.username == "admin"
    contraseña_valida = credenciales.password == "secret"
    if not (usuario_valido and contraseña_valida):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return credenciales.username

@app.get("/api/protegida")
def ruta_protegida(usuario: str = Depends(verificar_credenciales)):
    return {"mensaje": f"Acceso concedido a {usuario}!"}
