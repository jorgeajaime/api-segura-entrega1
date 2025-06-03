from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
API_KEY = "clave-secreta"

@app.get("/api/apikey")
async def api_con_apikey(x_api_key: str = Header(..., description="Clave API necesaria para acceder")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return {"mensaje": "Acceso autorizado por API Key"}
