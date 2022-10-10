const estado = document.getElementById("estado");
const solicitud = document.getElementById("solicitud");
function verificadDisponibilidad(){
    if(document.getElementById('estado').value=='En prestamo'){
        solicitud.classList.add("btn btn-danger");
        solicitud.classList.remove("btn btn-success");
    }
}
const boton = document.getElementById("boton");

function solicitudLibro(){
    
}

boton.addEventListener('click',true)
