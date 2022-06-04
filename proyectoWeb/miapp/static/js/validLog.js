function validar(){
	var todo_correcto = true;

	if(document.getElementById('username').value.length < 4 || document.getElementById('username') == ''){
		todo_correcto = false;
	}

	var expresion = /^[a-z][\w.-]+@\w[\w.-]+\.[\w.-]*[a-z][a-z]$/i;
	var email = document.form.email.value;
	if (!expresion.test(email)){
		todo_correcto = false;
	}

	if(document.getElementById('password').value == ''){
		todo_correcto = false;
	}

	if(!todo_correcto){
	alert('Algunos campos no están correctos, vuelva a revisarlos');
	}
	
	return todo_correcto;
	}