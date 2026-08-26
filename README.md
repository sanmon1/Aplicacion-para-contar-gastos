# 💰 Gestor de Gastos

Aplicación **full-stack** para registrar y controlar gastos personales. Backend hecho en **Python (Flask)** con base de datos **SQLite**, y frontend en **HTML, CSS y JavaScript**, con un diseño inspirado en un ticket/boleta de compra.

 ##✨ Características

- ➕ Agregar gastos (categoría, monto, descripción y fecha)
- 📄 Ver todos los gastos guardados, en tiempo real
- 🗑️ Eliminar un gasto
- 💵 Cálculo automático del total gastado
- 🎨 Diseño propio tipo "recibo de compra", con tipografía monoespaciada
- 🔗 API REST propia (CRUD completo) consumida desde el frontend con `fetch`

- # 🛠 Tecnologías

**Backend**
- Python 3
- Flask
- SQLite (`sqlite3`, incluido en Python)
- Flask-CORS

**Frontend**
- HTML5
- CSS3
- JavaScript (Vanilla JS, `fetch`, `async/await`)
- Google Fonts (Space Mono)

---

## ⚙️ Instalación

### 1. Cloná el repositorio

```bash
git clone https://github.com/sanmon1/gestor-gastos.git
cd gestor-gastos
```

### 2. Backend (Python)

Creá y activá un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux
```

Instalá las dependencias:

```bash
pip install flask flask-cors
```

Corré el servidor:

```bash
python app.py
```

El backend queda corriendo en `http://127.0.0.1:5000`.

### 3. Frontend

Abrí la carpeta `Frontend/` con la extensión **Live Server** de VS Code (clic derecho sobre `index.html` → "Open with Live Server"), o cualquier servidor local de tu preferencia.

> ⚠️ Frontend y backend corren en puertos distintos, por eso el proyecto usa **Flask-CORS** para permitir la comunicación entre ambos.

---

## 🚀 Uso

1. Con el backend y el frontend corriendo, abrí la página del frontend en el navegador.
2. Completá el formulario (categoría, monto, descripción, fecha) y hacé clic en **"+ Agregar gasto"**.
3. El gasto aparece al instante en la lista, y el total se actualiza automáticamente.
4. Para eliminar un gasto, hacé clic en el botón **✕** de la fila correspondiente.

---

## 🌐 Endpoints de la API

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/gastos` | Devuelve todos los gastos guardados |
| `POST` | `/gastos` | Crea un gasto nuevo |
| `PUT` | `/gastos/<id>` | Actualiza un gasto existente |
| `DELETE` | `/gastos/<id>` | Elimina un gasto |

## 👤 Autor

**sanmon1**
- GitHub: [@sanmon1](https://github.com/sanmon1)

