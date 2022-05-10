function validEmail(form) {
	Ctrl = form.email;
	if (Ctrl.value == "" || Ctrl.value.indexOf ('@', 0) == -1) {
		validatePrompt (Ctrl, "Ingresa un correo válido.")
		return (false);
	} else
		return (true);
}
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

