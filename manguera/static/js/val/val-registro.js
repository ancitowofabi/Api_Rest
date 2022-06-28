
$(function(){
    $("#formregistro").validate({
        rules: {
            nombre: "required",
            email: {
                required: true,
                email: true
            },
            contra: "required"
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
                minlength: 'Cantidad de digitos insuficiente'
            },
            contra:{
                required: 'Ingrese una Contraseña',
                minlength: 'Cantidad de caracteres insuficiente'
            }
        },
        submitHandler: function(form) {
            window.location.href='./index.html'
        }
    });
});