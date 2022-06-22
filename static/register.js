var script = document.createElement('script');
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

$('.txt_contrasena1').click(function(){
  $('.txt_contrasena1').removeClass(' border-danger')
  $('.txt_contrasena2').removeClass(' border-danger')
})

$(document).ready(function () {
  
  $("#txt_run")
  .rut({formatOn: 'keyup', validateOn: 'keyup'})
  .on('rutInvalido', function(){ 
    $(this).addClass(" border-danger")
    validacionRun = false
  })
  .on('rutValido', function(){ 
    $(this).removeClass("border-danger")
    $(".msj_validarRun").remove()
    validacionRun = true
  });

  $( ".txt_contrasena1" ).keyup(function(){
    $(".msj_validarContrasena").remove()
    $('.txt_contrasena1').removeClass(' border-danger')
    $('.txt_contrasena2').removeClass(' border-danger')
  })
  $( ".txt_correo1" ).keyup(function(){
    $(".msj_validarCorreo").remove()
    $('.txt_correo1').removeClass(' border-danger')
    $('.txt_correo2').removeClass(' border-danger')
  })
  $( ".txt_contrasena2" ).keyup(function(){
    $(".msj_validarContrasena").remove()
    $('.txt_contrasena1').removeClass(' border-danger')
    $('.txt_contrasena2').removeClass(' border-danger')
  })
  $( ".txt_correo2" ).keyup(function(){
    $(".msj_validarCorreo").remove()
    $('.txt_correo1').removeClass(' border-danger')
    $('.txt_correo2').removeClass(' border-danger')
  })

  $('#form_register').submit(function (e) {
    e.preventDefault()
    
    if ($('.txt_contrasena1').val() ==$('.txt_contrasena2').val() && validacionRun && $('.txt_correo1').val() ==$('.txt_correo2').val() ) {
      $.ajax({
        type: 'POST',
        url: "/clientes/registrarse/guardar",
        data: $(this).serialize(),
        datatype:'json',
        success: function (result) {
          console.log("result:", result);
        },
        error: function (err) {
          console.log("error: ", err);
        }
      });
    }else{
      if (validacionContrasena) {
        $('.txt_contrasena1').addClass(' border-danger')
        $('.txt_contrasena2').addClass(' border-danger')
        $("div.div_submit").prepend("<div class='msj_validarContrasena text-danger mb-2'><span>Las contraseñas no coinciden</span></div>")
        validacionContrasena = false
      }
      if (validacionCorreo) {
        $('.txt_correo1').addClass(' border-danger')
        $('.txt_correo2').addClass(' border-danger')
        $("div.div_submit").prepend("<div class='msj_validarCorreo text-danger mb-2'><span>Los correos no coinciden</span></div>")
        validacionCorreo = false
      }
      if(!validacionRun){
        $("div.div_submit").prepend("<div class='msj_validarRun text-danger  mb-2'><span>El formato del run no es correcto</span></div>")
      }
      
    }
    

  })
})
