function validNombre(form) {
	Ctrl = form.username;
	if (Ctrl.value.length == "") {
		validatePrompt (Ctrl, "Ingresa un nombre de usuario.")
		return (false);
	} else
		return (true);
}
function validPass(form) {
	Ctrl = form.password;
	if (Ctrl.value.length == "") {
		validatePrompt (Ctrl, "Ingresa una contraseña.")
		return (false);
	} else
		return (true);
}

function validaMail(input) {
	if (input.value == "" || input.value.indexOf('@', 0) == -1) {
	  input.setCustomValidity('"' + input.value + '" no es un correo válido.');
	} else {
	  input.setCustomValidity('');
	}
  }
 
  function valida_envia(){
	//valido el nombre
	if (document.registro.email.value.length==0 || document.getElementById('correo').indexOf ){
		   alert("Ingresa un correo válido")
		   document.fvalida.nombre.focus()
		   return 0;
	}
}