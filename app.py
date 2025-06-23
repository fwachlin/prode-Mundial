from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/pronostico", methods=["POST"])
def recibir_pronostico():
    data = request.json
    return jsonify({
        "mensaje": "Pronóstico recibido",
        "data": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
