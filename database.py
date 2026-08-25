import sqlite3

def conectar():
    conexion = sqlite3.connect("gastos.db")
    return conexion

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            monto REAL NOT NULL,
            descripcion TEXT,
            fecha TEXT
        )
    """)
    conexion.commit()
    conexion.close()

def insertar_gasto(categoria, monto, descripcion, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO gastos (categoria, monto, descripcion, fecha) VALUES (?, ?, ?, ?)",
        (categoria, monto, descripcion, fecha)
    )
    conexion.commit()
    conexion.close()


def obtener_todos_los_gastos():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM gastos")
        filas = cursor.fetchall()
        conexion.close()

        gastos = []
        for fila in filas:
            gastos.append({
                "id": fila[0],
                "categoria": fila[1],
                "monto": fila[2],
                "descripcion": fila[3],
                "fecha": fila[4]
            })  

        return gastos

def eliminar_gasto(id_gasto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM gastos WHERE id = ?", (id_gasto,))
    conexion.commit()
    conexion.close()

def actualizar_gasto(id_gasto, categoria, monto, descripcion, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
         "UPDATE gastos SET categoria = ?, monto = ?, descripcion = ?, fecha = ? WHERE id = ?", 
         (categoria, monto, descripcion, fecha, id_gasto)
         )
    conexion.commit()
    conexion.close()
