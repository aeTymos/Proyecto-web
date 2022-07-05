let updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var idProducto = this.dataset.producto
        var action = this.dataset.action
        console.log('idProducto: ', idProducto, 'action: ', action);

        console.log('USER: ', user);
        if (user === 'AnonymousUser') {
            console.log('')
        }            
    });
}