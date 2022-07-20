$('#loader').hide()
$(document).ready(function(){
    $("#img_fotosTrabajos").fileinput({
        maxFileCount: 4,
        validateInitialCount: true,
        overwriteInitial: false,
        allowedFileExtensions: ["jpg", "jpeg"]
    });

    $("#img_fotosTrabajos").on("filebatchselected", function(event, files) {
        if (files.length > 4) {
            //$('#input-pr').fileinput('destroy').fileinput({showPreview: true});
            $('#img_fotosTrabajos').fileinput('clear').fileinput('clearFileStack')
            Swal.fire({
                title: '¡Problemas!',
                text: 'El máximo de archivos es 4.',
                icon: 'error',
                confirmButtonText: 'Entendido'
              })
        }
    });
    var contadorServicios = 1
    $("#btn_agregarServicio").click(function(e){
        e.preventDefault();
        e.stopImmediatePropagation();
        contadorServicios++
        if (contadorServicios >= 10) {
            Swal.fire({
                title: '¡Problemas!',
                text: 'El máximo de servicios es 10.',
                icon: 'error',
                confirmButtonText: 'Entendido'
              })
        }else{
            $("#div_servicios").append(
                '<div class="row"> <div class="col"> <label for="txt_servicio'+contadorServicios+'">Nombre del servicio:</label> <input id="txt_servicio'+contadorServicios+'" name="txt_servicio'+contadorServicios+'" placeholder="Ej: Ampliación" class="form-control" type="text"> </div> <div class="col"> <label for="txt_valorServicio'+contadorServicios+'">Valor del servicio: </label> <input id="txt_valorServicio'+contadorServicios+'" name="txt_valorServicio'+contadorServicios+'" placeholder="Ej: 1000000" class="form-control" type="text"> </div> </div>'
            )
        }
    })
    
    $("#form_configPerfil").submit(function(e){
        var form = new FormData(this);
        form.append('foto1:',$("#img_fotosTrabajos")[0].files[0])
        form.append('foto2:',$("#img_fotosTrabajos")[0].files[1])
        form.append('foto3:',$("#img_fotosTrabajos")[0].files[2])
        form.append('foto4:',$("#img_fotosTrabajos")[0].files[3])
        form.append('fotoPerfil:',$("#img_fotoPerfil")[0].files[0])
        form.append('fotoPortada:',$("#img_fotoPortada")[0].files[0])
        $.ajax({
            type: "post",
            url: "/especialistas/configPerfil",
            data: form,
            dataType: 'json',
            cache:false,
            contentType:false,
            processData:false,
            success: function (url) {
                console.log('url: ', url);
                $('#msjLoader').html('¡Listo!').append('<h5 class="text-primary">Redirigiendo...</h5>');
                setTimeout(function () {
                  $('#loader').hide();
                  window.location.href = url
                }, 2000);
              },
              error: function (err) {
                console.log('err: ', err);
                $('#msjLoader').html('Algo ha salido mal...').append('<h5 class="text-primary">Vuelva a intentarlo</h5>');
                setTimeout(function () {
                  $('#loader').hide();
                }, 2000);
              }
        });
    })
})