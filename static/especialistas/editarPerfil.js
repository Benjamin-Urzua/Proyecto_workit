$("#btn_editarCarrusel").hide()
$("#btn_editarServicios").hide()
$("#btn_editarDescripcion").hide()
$("#btn_guardarCambios").hide()
$("#lbl_editarFotoPerfil").hide()
$("#lbl_editarFotoPortada").hide()

const eliminarServicio = cont => $("#btn_eliminarServicio"+cont+"").click(function(event) {$("#servicio"+cont+"").remove();});

$(document).ready(function () {

    
    $("#btn_habilitarEdicion").click(function () {
        $("#txt_descripcion").removeAttr("readonly")
        $("#row_carrusel").removeClass('mt-5')
        $("#btn_editarCarrusel").show()
        $("#btn_editarServicios").show()
        $("#btn_editarDescripcion").show()
        $("#lbl_editarFotoPerfil").show()
        $("#lbl_editarFotoPortada").show()
        $("#btn_guardarCambios").show()
        $(this).hide()
    })
    
    
    /*
    let btnImg = document.getElementById("lbl_img")

    var fotoPerfil

    btnImg.onchange = (event) => {
        var fd = new FormData()       
        fotoPerfil = document.getElementById("img_fotoPerfil")
        fotoPerfil.src = URL.createObjectURL(event.target.files[0])
        
            fd.append("file", event.target.files[0])
            fd.append("cloud_name", "<cloud name>")
            fd.append("upload_preset", "<upload preset>")
            console.log("imgsrc: ", img.src)
            console.log(fd)
            fetch('https://api.cloudinary.com/v1_1/dyqehknhi/workit/auto/upload',
            {
                method: 'POST',
                mode:"cors",
                body:fd
            }
            )
            

    }
    */

    var contadorServicios = Object.values($("#vars").data())[0]
    var nuevosServicios = []
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
                '<div class="row" id="servicio'+contadorServicios+'""> <div class="col-6"> <label for="txt_servicio'+contadorServicios+'">Nombre del servicio:</label> <input id="txt_servicio'+contadorServicios+'" name="txt_servicio'+contadorServicios+'" placeholder="Ej: Ampliación" class="form-control" type="text"> </div> <div class="col-5"> <label for="txt_valorServicio'+contadorServicios+'">Valor del servicio: </label> <input id="txt_valorServicio'+contadorServicios+'" name="txt_valorServicio'+contadorServicios+'" placeholder="Ej: 1000000" class="form-control" type="text"> </div> <div class="col-1"> <a type="button" id="btn_eliminarServicio'+contadorServicios+'"" class="mt-3 pt-1" onclick="eliminarServicio('+contadorServicios+')"><i style="font-size: 1.8rem;" class="bi bi-x-square-fill text-danger"></i></a></div></div>'
            )
        }
    })

    $("#btn_guardarFotos").click(function(e){
        e.preventDefault();
        e.stopImmediatePropagation();

        Swal.fire({
            title: '¡Éxito!',
            text: 'Sus fotos se han guardado',
            icon: 'success',
            confirmButtonText: 'Genial'
          })
    })
    $("#btn_guardarServicios").click(function(e){
        e.preventDefault();
        e.stopImmediatePropagation();

        Swal.fire({
            title: '¡Éxito!',
            text: 'Sus servicios se han guardado',
            icon: 'success',
            confirmButtonText: 'Genial'
          })
    })
    $("#input_fotoPerfil").change(function(){
        document.getElementById('img_fotoPerfil').src = URL.createObjectURL($(this)[0].files[0])
    })

    $("#btn_guardarCambios").click(function () {
        let descripcion = $("#txt_descripcion").val()
        var SendInfo = { SendInfo: [fotoPerfil.src, descripcion] }

        console.log(SendInfo)
        $.ajax({
            type: 'post',
            url: '/especialistas/perfil',
            data: JSON.stringify(SendInfo),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (response) {
                console.log(response)
            }
        });
    })


})