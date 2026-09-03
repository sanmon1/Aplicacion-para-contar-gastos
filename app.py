from flask import Flask, jsonify, request, render_template
from database import crear_tabla, insertar_gasto,obtener_todos_los_gastos, eliminar_gasto, actualizar_gasto
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

crear_tabla()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gastos")
def obtener_gastos():
    gastos = obtener_todos_los_gastos()
    return jsonify(gastos)

@app.route("/gastos", methods=["POST"])
def agregar_gasto():
    datos = request.get_json()
    insertar_gasto(
        datos["categoria"],
        datos["monto"],
        datos["descripcion"],
        datos["fecha"]
    )
    return jsonify({"mensaje": "Gasto agregado correctamente"}), 201

@app.route("/gastos/<int:id_gasto>", methods=["DELETE"])
def borrar_gasto(id_gasto):
    eliminar_gasto(id_gasto)
    return jsonify({"mensaje": "Gasto eliminado correctamente"}), 200

@app.route("/gastos/<int:id_gasto>", methods=["PUT"])
def modificar_gasto(id_gasto):
    datos = request.get_json()
    actualizar_gasto(
        id_gasto,
        datos["categoria"],
        datos["monto"],
        datos["descripcion"],
        datos["fecha"]
    )
    return jsonify({"mensaje": "Gasto actualizado correctamente"}), 200
if __name__ == "__main__":
    app.run(debug=True)


