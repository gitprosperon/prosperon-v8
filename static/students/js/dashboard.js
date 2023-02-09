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


    var carrotImage = a.children[1]

    if(element.style.display === 'flex') {
        element.style.display = 'none'
        carrotImage.style.transform = 'rotate(0deg)'
    } else if (element.style.display === 'none') {
        element.style.display = 'flex'
        carrotImage.style.transform = 'rotate(90deg)'
    }
}

// for removing subscription
function removeSubscription() {
    this.parentElement.parentElement.parentElement.style.display = 'none'
    console.log('remove the bitch')

    var price = this.parentElement.parentElement.children[2].children[0].innerHTML



    var elm = this
    var sub_transaction_id = this.id
    var token = this.parentElement.parentElement.parentElement.children[0].value
    $.ajax({
      type: "POST",
      url: '/university/budget/remove-subscription',
      data: {
          csrfmiddlewaretoken: token,
          action: "post",
          dummy: "fucker",
          transaction_id: sub_transaction_id,
          monthly_price

        }

    })

}


const elements = document.getElementsByClassName('back-btn remove-subscription')

for(let i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', removeSubscription)
}