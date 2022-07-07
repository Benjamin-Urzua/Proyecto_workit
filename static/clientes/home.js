$(document).ready(function () { //Mandar otro mensaje para confirmar
    $('#loader').hide()
    $('#btn_eliminarCuenta').click(function(){
        $('.modal-dialog').show()
        $('#btn_modalContinuar').click(function(){
            $('.modal-body').html("<div class='form-group  d-flex justify-content-center'> <input type='email' class='form-control' id='txt_correo' name='txt_correo' placeholder='Ingrese su correo'> </div> <div class='form-group d-flex justify-content-center mt-2'>  <input type='password' class='form-control' id='txt_contrasena' name='txt_contrasena' placeholder='Ingrese su contraseña'> </div>")
            $(this).replaceWith("<button type='submit' class='btn btn-danger' id='btn_submit'>Aceptar</button>")
        })
        $('#form_eliminarCuenta').submit(function(e){
            e.preventDefault()
            e.stopImmediatePropagation();
            $.ajax({
                type: 'POST',
                url: "/clientes/eliminarCuenta",
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
                        if (result["Codigo"] == -1){
                            $('#msjLoader').html(""+result["Msj"]).append('<h5 class="text-primary">Vuelva a intentarlo...</h5>')
                            setTimeout(function () {
                                $('#loader').hide();
                            }, 1000)
                        }else{
                            $('#msjLoader').html(""+result["Msj"]).append('<h5 class="text-primary">Vuelva a intentarlo...</h5>')
                            setTimeout(function () {
                                $('#loader').hide();
                            }, 1000)
                        }
                        
                    }
                },
                error: function (err) {
                    $('#loader').hide();
                    console.log("error: ", err);
                }
            });
        })
    })
})