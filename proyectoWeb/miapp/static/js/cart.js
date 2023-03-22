let updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        let idProducto = this.dataset.producto
        let action = this.dataset.action
        console.log('idProducto: ', idProducto, 'action: ', action);

        console.log('USER: ', user);
        if (user === 'AnonymousUser') {
            console.log('Usuario no ha ingresado sesión.');
        } else{
            actualizaPedidoUsuario(idProducto, action) 
        }            
    });
}

function actualizaPedidoUsuario(idProducto, action) {
    console.log('Usuario ingresó sesión. Enviando datos...');
    let url = '/actualiza-producto/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'idProducto': idProducto, 'action': action})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data: ', data);
    })
}
