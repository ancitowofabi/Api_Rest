
$(function(){
    $("#formcontacto").validate({
        rules: {
            nombre: "required",
            email: {
                required: true,
                email: true
            },
            telefono: "required",
            mensaje: "required"
            
        },
        messages: {
            nombre:{
                required: 'Ingrese su nombre'
            },
            email: {
                required: 'Ingrese su correo electrónico',
                email: 'Formato de correo no válido'
            },
            telefono:{
                required: 'Ingrese un número de celular',
                minlength: 'Cantidad de digitos insuficiente'
            },
            mensaje:{
                required: 'Ingrese un mensaje a enviar'
            }
        },
        submitHandler: function(form) {
            window.location.href='./index.html'
        }
    });
});
