var elements = document.getElementsByClassName('text-field')
for (let i = 0; i < elements.length; i++) {
    if(elements[i].value === 'None') {
        elements[i].value = ''
    }
}





function showNextForm(){
    var first = document.getElementById('first-question')
    var second = document.getElementById('second-question')
    first.style.display = 'none';
    second.style.display = 'flex'
}


function showBackForm() {
    var first = document.getElementById('first-question')
    var second = document.getElementById('second-question')
    first.style.display = 'flex';
    second.style.display = 'none'
}



