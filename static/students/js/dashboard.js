

function moreInformationToggle(a) {
    var element = a.parentElement.children[1]


    var carrotImage = a.children[1]

    if(element.style.display === 'block') {
        element.style.display = 'none'
        carrotImage.style.transform = 'rotate(0deg)'
    } else if (element.style.display === 'none') {
        element.style.display = 'block'
        carrotImage.style.transform = 'rotate(90deg)'
    }
}

// for removing subscription
function removeSubscription() {
    this.parentElement.parentElement.parentElement.style.display = 'none'
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
          monthly_price: price
        }
    })
}
const elements = document.getElementsByClassName('back-btn remove-subscription')
for(let i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', removeSubscription)
}


function changeSpendingHabit() {
    console.log('change spending habit')
    var theSelectedIndex = this.parentElement.children[1].options.selectedIndex
    var token = this.parentElement.parentElement.children[0].children[0].value
    var tran_id = this.id
    if (theSelectedIndex !== 0) {
        var selectedValue = this.parentElement.children[1].options[theSelectedIndex].value
        $.ajax({
          type: "POST",
          url: '/university/budget/update_spending_habit',
          data: {
              csrfmiddlewaretoken: token,
              action: "post",
              transaction_id: tran_id,
              new_range: selectedValue
            }
        })
    } else {
        console.log('user needs to select range')
    }
}

const spendingHabitElements = document.getElementsByClassName('next-btn spending-habit')
for(let i = 0; i < spendingHabitElements.length; i++) {
    spendingHabitElements[i].addEventListener('click', changeSpendingHabit)
}