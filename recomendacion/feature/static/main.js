console.log('hello world')


const spinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')

//console.log(spinnerBox)
//console.log(dataBox)

$.ajax({
    type: 'POST',
    url: '/recomendacion',
    success: function(response){
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
            console.log('response',response )
        }, 5000)

    },
    error: function(error){
        console.log(error)
    }
})