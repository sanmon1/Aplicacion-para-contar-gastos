const URL_BASE = "";

const form = document.getElementById("form-gasto");
const listaGastos = document.getElementById("lista-gastos");
const totalSpan = document.getElementById("total");

document.addEventListener("DOMContentLoaded", cargarGastos);

form.addEventListener("submit", async (evento) => {
evento.preventDefault();

const gastoNuevo = {
    
    categoria: document.getElementById("categoria").value,
    descripcion: document.getElementById("descripcion").value,
    monto: parseFloat(document.getElementById("monto").value),
    fecha: document.getElementById("fecha").value
};

await fetch(`${URL_BASE}/gastos`, {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify(gastoNuevo)
});

form.reset();
cargarGastos();

});


async function cargarGastos() {
    const respuesta = await fetch(`${URL_BASE}/gastos`);
    const gastos = await respuesta.json();

    listaGastos.innerHTML = "";
    let total = 0;

    gastos.forEach((gasto) => {
        total += gasto.monto;

        const div = document.createElement("div");
        div.classList.add("gasto");
        div.innerHTML = `
            <div class="gasto__info">
                <span class="gasto__categoria">${gasto.categoria}</span>
                <span class="gasto__meta">${gasto.descripcion || "sin descripción"} · ${gasto.fecha}</span>
            </div>
            <span class="gasto__monto">$${gasto.monto.toFixed(2)}</span>
            <button class="gasto__borrar" onclick="borrarGasto(${gasto.id})" aria-label="Borrar gasto">✕</button>
        `;
        listaGastos.appendChild(div);
    });

    totalSpan.textContent = total;
}

async function borrarGasto(id) {
    await fetch(`${URL_BASE}/gastos/${id}`, {
        method: "DELETE"
    });
    cargarGastos();
}