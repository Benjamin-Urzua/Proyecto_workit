/*var script = document.createElement('script');
var near_place;
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDM-j--qFSEiW1KzVtL_3kMZo9gh4cGXr8&libraries=places&callback=initMap';
script.async = true;
var validacionContrasena = true
var validacionCorreo = true
var validacionRun = false


window.initMap = function () {
  var autocompletadoMaps;
  autocompletadoMaps = new google.maps.places.Autocomplete((document.getElementById('txt_direccion')), {
    types: ['geocode'],
  });

  google.maps.event.addListener(autocompletadoMaps, 'place_changed', function () {
    near_place = autocompletadoMaps.getPlace();
  });
};
document.head.appendChild(script);
*/

var validacionContrasena=true
var validacionRun = false

$('.txt_contrasena1').click(function () {
  $('.txt_contrasena1').removeClass(' border-danger')
  $('.txt_contrasena2').removeClass(' border-danger')
})


$(document).ready(function () {
  cargarRegion();

  $("#combo_region").change(function(){
    if($(this).val() != ''){
      $( "#combo_provincia" ).prop( "disabled", false );
      cargarProvincia();
    }
  })
  
  $("#combo_provincia").change(function(){
    if($(this).val() != ''){
      $( "#combo_comuna" ).prop( "disabled", false );
      cargarComuna();
    }
  })
  

  function cargarRegion(){
    var opciones = "<option value='' selected>Seleccione una región</option>"

    $.ajax({
      url:'https://apis.digital.gob.cl/dpa/regiones',
      dataType:'JSON',
      success:function(regiones){
        $.each(regiones,function(i,region){
          opciones+="<option value='"+region.codigo+"'>"+region.nombre+"</option>";
        });
        $("#combo_region").html(opciones);
      }
    });
  }
  
  function cargarProvincia(){
    var opciones = "<option value='' selected>Seleccione una provincia</option>"

    $.ajax({
      url:`https://apis.digital.gob.cl/dpa/regiones/${$('#combo_region').val()}/provincias`,
      dataType:'JSON',
      success:function(provincias){
        $.each(provincias,function(i,provincia){
          opciones+="<option value='"+provincia.codigo+"'>"+provincia.nombre+"</option>";
        });
        $("#combo_provincia").html(opciones);
      }
    });
  }

  function cargarComuna(){
    var opciones = "<option value='' selected>Seleccione una comuna</option>"

    $.ajax({
      url:`https://apis.digital.gob.cl/dpa/provincias/${$('#combo_provincia').val()}/comunas`,
      dataType:'JSON',
      success:function(comunas){
        $.each(comunas,function(i,comuna){
          opciones+="<option value='"+comuna.codigo+"'>"+comuna.nombre+"</option>";
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
    $('.txt_contrasena2').removeClass(' border-danger')
  })
  
  $(".txt_contrasena2").keyup(function () {
    $(".msj_validarContrasena").remove()
    $('.txt_contrasena1').removeClass(' border-danger')
    $('.txt_contrasena2').removeClass(' border-danger')
  })
  

  $('#form_register').submit(function (e) {
    e.preventDefault()
    
    if ($('.txt_contrasena1').val() == $('.txt_contrasena2').val() && validacionRun) {
      $.ajax({
        type: 'POST',
        url: "/clientes/registrarse/guardar",
        data: $(this).serialize(),
        datatype: 'json',
        success: function (result) {
          console.log("result:", result);
        },
        error: function (err) {
          console.log("error: ", err);
        }
      });
    } else {
      if (validacionContrasena) {
        $('.txt_contrasena1').addClass(' border-danger')
        $('.txt_contrasena2').addClass(' border-danger')
        $("div.div_submit").prepend("<div class='msj_validarContrasena text-danger mb-2'><span>Las contraseñas no coinciden</span></div>")
        validacionContrasena = false
      }
      if (!validacionRun) {
        $("div.div_submit").prepend("<div class='msj_validarRun text-danger  mb-2'><span>El formato del run no es correcto</span></div>")
      }

    }


  })
})
