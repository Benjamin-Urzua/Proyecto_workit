$("#btn_modificarDescripcion").hide()
$("#lbl_editarFotoPerfil").hide()
$("#btn_guardarCambios").hide()

$(document).ready(function(){
 $("#btn_habilitarEdicion").click(function(){
        $("#txt_descripcion").removeAttr("readonly")
        $("#btn_modificarDescripcion").show()
        $("#lbl_editarFotoPerfil").show()
        $("#btn_guardarCambios").show()
        $(this).hide()
    })

    let btnImg = document.getElementById("lbl_img")
    
    var fotoPerfil

    btnImg.onchange = (event) => {
        //var fd = new FormData()       
        fotoPerfil = document.getElementById("img_fotoPerfil")
        fotoPerfil.src = URL.createObjectURL(event.target.files[0])
    /*
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
        */
        
    }

    $("#btn_guardarCambios").click(function () { 
        let descripcion = $("#txt_descripcion").val()
        var SendInfo = { SendInfo : [fotoPerfil.src, descripcion]}
        
        console.log(SendInfo)
        $.ajax({
           type: 'post',
            url: '/clientes/perfil',
            data: JSON.stringify(SendInfo),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (response) {
                console.log(response)
            }
        });
     })

    
})