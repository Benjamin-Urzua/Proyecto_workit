var validacionContasenaVacia = true
var validacionRun = false
var validacionCorreo = true
var validacionLongContrasena = true


$("#form_paso2").hide()
$("#btn_submit").hide()
$("#btn_volver").hide()
$('#loader').hide()

$(document).ready(function () {
  cargarRegion();

  $('.txt_contrasena1').click(function () {
    $('.txt_contrasena1').removeClass(' border-danger')
    $('.txt_contrasena2').removeClass(' border-danger')
  })
  $("#combo_region").change(function () {
    if ($(this).val() != '') {
      $("#combo_provincia").prop("disabled", false);
      cargarProvincia();
    }
  })

  $("#combo_provincia").change(function () {
    if ($(this).val() != '') {
      $("#combo_comuna").prop("disabled", false);
      cargarComuna();
    }
  })


  function cargarRegion() {
    var opciones = "<option value='' selected>Seleccione una región</option>"

    $.ajax({
      
      type:'GET',
      url: 'https://apis.digital.gob.cl/dpa/regiones',
      dataType: 'JSON',
      success: function (regiones) {
        $.each(regiones, function (i, region) {
          opciones += "<option value='" + region.codigo + "'>" + region.nombre + "</option>";
        });
        $("#combo_region").html(opciones);
      }
    });
  }

  function cargarProvincia() {
    var opciones = "<option value='' selected>Seleccione una provincia</option>"

    $.ajax({
      type:'GET',
      url: `https://apis.digital.gob.cl/dpa/regiones/${$('#combo_region').val()}/provincias`,
      dataType: 'JSON',
      success: function (provincias) {
        $.each(provincias, function (i, provincia) {
          opciones += "<option value='" + provincia.codigo + "'>" + provincia.nombre + "</option>";
        });
        $("#combo_provincia").html(opciones);
      }
    });
  }

  function cargarComuna() {
    var opciones = "<option value='' selected>Seleccione una comuna</option>"

    $.ajax({
      url: `https://apis.digital.gob.cl/dpa/provincias/${$('#combo_provincia').val()}/comunas`,
      dataType: 'JSON',
      success: function (comunas) {
        $.each(comunas, function (i, comuna) {
          opciones += "<option value='" + comuna.codigo + "'>" + comuna.nombre + "</option>";
        });
        $("#combo_comuna").html(opciones);
      }
    });
  }

  $("#txt_run")
    .rut({ formatOn: 'keyup', validateOn: 'keyup' })
    .on('rutInvalido', function () {
      $(this).addClass(" border-danger")
      validacionRun = false
    })
    .on('rutValido', function () {
      $(this).removeClass("border-danger")
      $(".msj_validarRun").remove()
      validacionRun = true
    });

  $(".txt_contrasena1").keyup(function () {
    $(".msj_validarContrasena").remove()
    $('.txt_contrasena1').removeClass(' border-danger')
  })

  $(".txt_correo").keyup(function () {
    $(".msj_validarCorreo").remove()
    $('.txt_correo').removeClass(' border-danger')
  })

  $("#btn_pasoSiguiente").click(function () {
    if (($('.txt_contrasena1').val() != "") && ($('.txt_contrasena1').val().length >= 8) && ($('.txt_correo').val().includes("@") && $('.txt_correo').val().includes(".")) && validacionRun) {
      $("#form_paso1, #btn_pasoSiguiente").fadeTo(500, 0, function () {
        $(this).hide()
        $("#form_paso2, #btn_submit, #btn_volver").fadeTo(500, 1).show()
      })
    } else {
      if ($('.txt_contrasena1').val() == "" || $('.txt_contrasena2').val() == "") {
        if (validacionContasenaVacia) {
          $('.txt_contrasena1').addClass(' border-danger')
          $('.txt_contrasena2').addClass(' border-danger')
          $("div.div_submit").prepend("<div class='msj_validarContrasena text-danger mb-2'><span>Ingrese su contraseña.</span></div>")
          validacionContasenaVacia = false
        }
      } else if (!($('.txt_correo').val().includes("@")) || !($('.txt_correo').val().includes("."))) {
        if (validacionCorreo) {
          $('.txt_correo').addClass(' border-danger')
          $("div.div_submit").prepend("<div class='msj_validarCorreo text-danger mb-2'><span>El formato del correo es incorrecto.</span></div>")
          validacionCorreo = false
        }
      } else if (!validacionRun) {
        $("div.div_submit").prepend("<div class='msj_validarRun text-danger  mb-2'><span>El formato del run no es correcto</span></div>")
      }
      else {
        if (validacionLongContrasena) {
          $('.txt_contrasena1').addClass(' border-danger')
          $('.txt_contrasena2').addClass(' border-danger')
          $("div.div_submit").prepend("<div class='msj_validarContrasena text-danger mb-2'><span>La contraseña debe contener al menos 8 caracteres.</span></div>")
          validacionLongContrasena = false
        }
      }
    }
  })

  $("#btn_volver").click(function () {

    $("#form_paso2, #btn_submit, #btn_volver").fadeTo(500, 0, function () {
      $(this).hide()
      $("#form_paso1, #btn_pasoSiguiente").fadeTo(500, 1).show()
    })
  })

  $('#form_register').submit(function (e) {
    e.preventDefault()
    e.stopImmediatePropagation();
    var form2 = new FormData(this);

    /*
    var fd = document.getElementById("form_register")  
   
    //form.append('form', $(this)[0])
    console.log('form: ', form)
   */
    $.ajax({
      type: 'POST',
      url: "/especialistas/registrarse/guardar",
      data: form2,
      dataType: 'json',
      cache:false,
      contentType:false,
      processData:false,
      beforeSend: function () {
        $('#loader').show();
      },
      success: function (url) {
        $('#msjLoader').html('¡Registrado correctamente!').append('<h5 class="text-primary">Redirigiendo...</h5>')
        setTimeout(function () {
          $('#loader').hide();
          window.location.href = url
        }, 2000)

      },
      error: function (err) {
        $('#msjLoader').html('Algo ha salido mal...').append('<h5 class="text-primary">Vuelva a intentarlo</h5>')
        setTimeout(function () {
          $('#loader').hide();
        }, 2000)
      }
    });




  })


})
