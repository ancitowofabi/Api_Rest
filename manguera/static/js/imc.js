function imc(){
    var peso = parseInt($('#peso').val()) || 0;
    var altura = parseInt($('#altura').val())/100 || 0;

    var imc = peso/(altura^2) || 0;
    if (imc == 0) return alert("Ingrese datos válidos")
    $('#imclabel').html(imc);

    if (imc<18.5)
        return $('#imctablelabel').html("inferior al normal.");
    if (imc<24.9)
        return $('#imctablelabel').html("normal.");
    if (imc<29.9)
        return $('#imctablelabel').html("superior al normal.");
    else
        return $('#imctablelabel').html("obeso.");

        

}