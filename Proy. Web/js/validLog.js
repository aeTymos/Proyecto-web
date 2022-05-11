/*function validaNombre(form) {
	Ctrl = form.username;
	if (Ctrl.value.length == "") {
		validatePrompt (Ctrl, "Ingresa un nombre de usuario.")
		return (false);
	} else
		return (true);
}
function validaPass(form) {
	Ctrl = form.password;
	if (Ctrl.value.length == "") {
		validatePrompt (Ctrl, "Ingresa una contraseña.")
		return (false);
	} else
		return (true);
}
*/
function validaMail(input) {
	if (input.value == "" || input.value.indexOf('@', 0) == -1) {
	  input.setCustomValidity('"' + input.value + '" no es un correo válido.');
	} else {
	  input.setCustomValidity('');
	}
  }
 
 