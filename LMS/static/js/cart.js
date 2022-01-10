var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var laundryId = this.dataset.laundry
        var action = this.dataset.action
        console.log('laundryId:', laundryId, 'action:', action )

        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(laundryId, action)
        }
    })
}

function updateUserOrder(laundryId, action){
    console.log('user is logged in sending data')

    var url = '/update_item'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'laundryId': laundryId, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
    })
}