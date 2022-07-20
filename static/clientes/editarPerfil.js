$("#lbl_editarFotoPerfil").hide()
$("#btn_guardarCambios").hide()


$(document).ready(function () {
    $("#btn_habilitarEdicion").click(function () {
        $("#txt_descripcion").removeAttr("readonly")
        $("#lbl_editarFotoPerfil").show()
        $(this).hide()
        $("#btn_guardarCambios").show()
        
    })
    $("#input_fotoPerfil").change(function(){
        document.getElementById('img_fotoPerfil').src = URL.createObjectURL($(this)[0].files[0])
    })
    
    $("#form_perfilCliente").submit(function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        var form = new FormData(this);
        form.append('fotoPerfil:',$("#input_fotoPerfil")[0].files[0])
        $.ajax({
            type: 'post',
            url: '/clientes/perfil',
            data: form,
            cache:false,
            contentType:false,
            processData:false,
            success: function (response) {
                Swal.fire({ 
                    title: 'Información',
                    text: response,
                    icon: 'info',
                    confirmButtonText: 'Entendido'
                  })
            }
        });
    })


})