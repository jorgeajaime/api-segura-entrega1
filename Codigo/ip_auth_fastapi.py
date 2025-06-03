from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

# Lista blanca de IPs autorizadas
IPS_PERMITIDAS = ["127.0.0.1", "192.168.0.10"]

@app.middleware("http")
async def verificar_ip(request: Request, call_next):
    ip_cliente = request.client.host
    if ip_cliente not in IPS_PERMITIDAS:
        raise HTTPException(status_code=403, detail="Acceso denegado: IP no autorizada")
    return await call_next(request)

@app.get("/api/ip_protegida")
def ruta_ip():
    return {"mensaje": "Acceso permitido desde una IP válida"}
