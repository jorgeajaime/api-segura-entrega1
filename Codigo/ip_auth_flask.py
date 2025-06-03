from flask import Flask, request, jsonify

app = Flask(__name__)

IP_PERMITIDA = "192.168.0.162"  # IP de tu PC

@app.route("/api/ip_protegida", methods=["GET"])
def ruta_ip_protegida():
    ip_cliente = request.remote_addr
    if ip_cliente != IP_PERMITIDA:
        return jsonify({"mensaje": "Acceso denegado desde esta IP"}), 403
    return jsonify({"mensaje": f"Acceso permitido desde {ip_cliente}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
