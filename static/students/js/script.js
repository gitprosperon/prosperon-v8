


// script for sidebar logic
function hideSidebar() {
   var sidebar = document.getElementById('sidebar')
    var right_col = document.getElementById('right-col')


    if (sidebar.style.display === 'block') {
       sidebar.style.display = 'none'
        right_col.style.width = "100" + '%'

    } else if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block'
        right_col.style.width = "80" + '%'

    }

}

// script for toggeling all video page
function videoToggle(a, information ) {
    var inforTarget = document.getElementById('video-info-target')
    var allButtons = document.getElementsByClassName('_18-poppins semibold centered-text')
    inforTarget.innerHTML = information

    for(let i = 0; i < allButtons.length; i++) {
        allButtons[i].className = '_18-poppins semibold centered-text'
    }
    a.className = '_18-poppins semibold centered-text clicked'



}


function transactionsToggle(a, target) {
    var elements = document.getElementsByClassName('filter-categories-wrapper')
    var showTarget = document.getElementById(target)
    var allShowTargets = document.getElementsByClassName('transactions-target-cards')

    for(let i = 0; i < elements.length; i++) {
        var elm = elements[i]
        elm.className = 'filter-categories-wrapper not-selected'
        a.className = 'filter-categories-wrapper selected'
    }

    for(let i = 0; i < allShowTargets.length; i++) {
        var showElm = allShowTargets[i]
        showElm.style.display = 'none'

    }

    var allTransactions = document.getElementsByClassName('_20-padding-container transaction-card')


    if(target === '1') {
        for(let i = 0; i < allTransactions.length; i++) {
            var all_target = allTransactions[i]
            console.log(all_target.children[1].children[1].children[0].children[0].children[0].children[3].children[0].style.display)
            allTransactions[i].style.display = 'flex'
    }


    } else if (target === '2' ) {
        console.log('completed')
        for(let i = 0; i < allTransactions.length; i++) {
            var all_target_completed = allTransactions[i]
            allTransactions[i].style.display = 'none'
            console.log(all_target_completed.children[1].children[1].children[0].children[0].children[0].children[3].children[0].style.display)
            if (all_target_completed.children[1].children[1].children[0].children[0].children[0].children[3].children[0].style.display === 'block') {
                allTransactions[i].style.display = 'flex'


            }

        }

    } else if (target === '3') {
        console.log('incompleted')
        for(let i = 0; i < allTransactions.length; i++) {
            var incomplete = allTransactions[i]
            allTransactions[i].style.display = 'none'
            console.log(incomplete.children[1].children[1].children[0].children[0].children[0].children[3].children[0].style.display)
            if (incomplete.children[1].children[1].children[0].children[0].children[0].children[3].children[0].style.display === 'none') {
                allTransactions[i].style.display = 'flex'

            }
        }
    }


    showTarget.style.display = 'block'

}

