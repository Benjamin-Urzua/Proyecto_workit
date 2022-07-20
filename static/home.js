$(document).ready(function () { //Mandar otro mensaje para confirmar
    $('#loader').hide()
    $('#btn_eliminarCuenta').click(function(){
        $('.modal-dialog').show()
        $('#btn_modalContinuar').click(function(){
            $('.modal-body').html("<div class='form-group  d-flex justify-content-center'> <input type='email' class='form-control' id='txt_correo' name='txt_correo' placeholder='Ingrese su correo'> </div> <div class='form-group d-flex justify-content-center mt-2'>  <input type='password' class='form-control' id='txt_contrasena' name='txt_contrasena' placeholder='Ingrese su contraseña'> </div>")
            $(this).replaceWith("<button type='submit' class='btn btn-danger' id='btn_submit'>Aceptar</button>")
        })
        $("#btn_cerrarSesion").click(function () {
            Swal.fire({
                title: '¡Genial!',
                text: 'Ha cerrado sesión correctamente',
                icon: 'success',
                confirmButtonText: 'Entendido'
              })
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
                    $("#modal").hide()
                    if (result["Codigo"] == 1) {
                        Swal.fire({
                            title: 'Procedimiento exitoso',
                            text: 'Su cuenta ha sido borrada y será redirigido',
                            icon: 'info',
                            confirmButtonText: 'Entendido'
                          })
                        setTimeout(function () {
                            $('#loader').hide();
                            window.location.href = result["Redirect"]
                        }, 2000)
                    }else{
                        if (result["Codigo"] == -1){
                            Swal.fire({
                                title: 'Algo salió mal',
                                text: 'Puede volver a intentarlo',
                                icon: 'warning',
                                confirmButtonText: 'Entendido'
                              })
                            setTimeout(function () {
                                $('#loader').hide();
                            }, 1000)
                        }else{
                            Swal.fire({
                                title: 'Algo salió mal',
                                text: 'Puede volver a intentarlo',
                                icon: 'warning',
                                confirmButtonText: 'Entendido'
                              })
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