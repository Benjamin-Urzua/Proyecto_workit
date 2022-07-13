$(document).ready(function () {
    $('#loader').hide()
    $('#form_login').submit(function (e) {
        e.preventDefault()
        e.stopImmediatePropagation();
        $.ajax({
            type: 'POST',
            url: "/especialistas/login/autentificacion",
            data: $(this).serialize(),
            datatype: 'json',
            beforeSend: function () {
                $('#loader').show();
            },
            success: function (result) {
                if (result["Codigo"] == 1) {
                    $('#msjLoader').html(""+result["Msj"]).append('<h5 class="text-primary">Redirigiendo...</h5>')
                    setTimeout(function () {
                        $('#loader').hide();
                        window.location.href = result["Redirect"]
                    }, 2000)
                }else{
                    $('#msjLoader').html(""+result["Msj"]).append('<h5 class="text-primary">Vuelva a intentarlo...</h5>')
                    setTimeout(function () {
                        $('#loader').hide();
                    }, 1000)
                }
            },
            error: function (err) {
                $('#loader').hide();
                console.log("error: ", err);
            }
        });
    })
})