
// Funcion para recibir un diccionario o mapa de errores
// y mostrarlo dentro de una alerta de SweetAlarm. Para
// que tenga efecto se necesita importar SweetAlarm primero
function message_error(obj) {

    var html = '';

    //Los errores pueden ser, errores de la base de datos (añadir un valor duplicado
    // en un campoq ue no lo permite o un numero en un campo que no es numerico), en ese caso
    // el error se retorna como un objeto de errores. Si el error es por sintaxis desde el lado
    // del servidor, el error se retorna como un simple String (ej: no se reconoce la función funcx).
    // Si el error es un String, entonces simplemente imprimir ese String dentro de un SweetAlert.

    // Si el error no es un simple string, sino un
    // objeto de errores entonces
    if (typeof (obj) === 'object') {

        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';

    // Si el error es un String entonces el html será sólo ese error
    } else {
        html = '<p>'+obj+'</p>';
    }

    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });

}