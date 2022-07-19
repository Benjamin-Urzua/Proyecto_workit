$("#btn_editarCarrusel").hide()
$("#btn_editarServicios").hide()
$("#btn_editarDescripcion").hide()
$("#lbl_editarFotoPerfil").hide()
$("#lbl_editarFotoPortada").hide()


$(document).ready(function () {
    

    
    $("#btn_habilitarEdicion").click(function () {
        $("#txt_descripcion").removeAttr("readonly")
        $("#row_carrusel").removeClass('mt-5')
        $("#btn_editarCarrusel").show()
        $("#btn_editarServicios").show()
        $("#btn_editarDescripcion").show()
        $("#lbl_editarFotoPerfil").show()
        $("#lbl_editarFotoPortada").show()
        $(this).text('Guardar cambios')
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