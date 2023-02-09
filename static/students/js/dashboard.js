function showSimulate(){
var simulateBtnTarget = document.getElementById('simulateBtn')
    simulateBtnTarget.style.display = 'block'

}

function simulateRun() {
    var selectIndex = this.parentElement.children[0].options.selectedIndex
    var selectedData = this.parentElement.children[0].options[selectIndex].value
    location.replace("/university/simulate/" + selectedData)

}

//
var simulateBtnTarget = document.getElementById('simulateBtn')
simulateBtnTarget.addEventListener('click', simulateRun)


function moreInformationToggle(a) {
    var element = a.parentElement.children[1]
    console.log(element)

    var carrotImage = a.children[1]

    if(element.style.display === 'flex') {
        element.style.display = 'none'
        carrotImage.style.transform = 'rotate(0deg)'
    } else if (element.style.display === 'none') {
        element.style.display = 'flex'
        carrotImage.style.transform = 'rotate(90deg)'
    }
}


function removeSubscription() {
    console.log(this.id)
}


const elements = document.getElementsByClassName('back-btn remove-subscription')


for(let i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', removeSubscription)
}