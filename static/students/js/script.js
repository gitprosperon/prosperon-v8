


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


// functionality for toggeling transactions on transactions page
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


// logic for toggeling subscriptions on spending profile
function subscriptionClick(a) {
    if(a.children[2].className === 'price-range-wrapper hidden') {
        a.children[2].className = 'price-range-wrapper'
    } else if (a.children[2].className === 'price-range-wrapper') {
        a.children[2].className = 'price-range-wrapper hidden'
    }
}


// logic for toggeling monthly expenses on spending profile
function monthly_expenseClick(a) {
    var selectedIndex = a.children[2].children[0].options.selectedIndex

    if(a.children[2].className === 'price-range-wrapper hidden') {
        a.children[2].className = 'price-range-wrapper'
        console.log(a.children[2].children[0].options.selectedIndex)
    } else {
        console.log('fucker123');
        a.children[0].onClick = function () {

        }
    }



     if(selectedIndex !== 0) {
        a.children[2].className = 'price-range-wrapper hidden'
    }
}


// logic for toggeling through spending profile page
var spendingProfileIndex = 0
function spender_profile_toggle(a){
    var spendingProfileTarget = document.getElementById('spending-profile-scale-container');
    var subscriptionsTarget = document.getElementById('subscriptions-container');
    var expensesTarget = document.getElementById('monthly-expenses-container');
    var conatinerList = [spendingProfileTarget, subscriptionsTarget, expensesTarget]

    // logic for if it is next
    if(a.innerHTML === 'Next') {
        console.log('go next')
        spendingProfileIndex += 1
        for(let i = 0; i < conatinerList.length; i++) {
            var elmID = conatinerList[i]
            elmID.style.display = 'none'
        }

        document.getElementById(conatinerList[spendingProfileIndex].id).style.display = 'block'

    // logic for if it is back
    } else if (a.innerHTML === 'Back') {
        console.log('go back')
        spendingProfileIndex += -1

        for(let i = 0; i < conatinerList.length; i++) {
            var elmID2 = conatinerList[i]
            elmID2.style.display = 'none'
        }
        document.getElementById(conatinerList[spendingProfileIndex].id).style.display = 'block'
    }

    console.log(spendingProfileIndex)
    var nextButtonToggle = document.getElementById('next-btn-toggle');
    var NextButtonWithLink = document.getElementById('next-btn');


    var backButtonToggle = document.getElementById('toggle-back-button')
    var backButtonWithLink = document.getElementById('back-button-with-link')


    if(spendingProfileIndex === 0) {
        console.log('equal to 0')
        backButtonToggle.style.display = 'none'
        backButtonWithLink.style.display = 'flex'

        var radioButtons = document.getElementsByClassName('w-form-formradioinput w-radio-input')

        // checking to see how many radio buttons are checked
        var numChecked = 0
        for(let i = 0; radioButtons.length; i++) {
            if (radioButtons[i].checked === true) {
                numChecked += 1
                console.log('it is checked')
            }
        }
    }
    if(spendingProfileIndex === 1) {
        backButtonToggle.style.display = 'flex'
        backButtonWithLink.style.display = 'none'
    }
    if(spendingProfileIndex === 2) {
        nextButtonToggle.style.display = 'none';
        NextButtonWithLink.style.display = 'flex';
    } else {
        nextButtonToggle.style.display = 'flex';
        NextButtonWithLink.style.display = 'none';
    }
}


// functionality for toggeling lycter scale questions
var LycterScalesIndex = 0
function toggleLycterScale(a) {
    var section1 = document.getElementById('lycterQuestionsFirst')
    var section2 = document.getElementById('lycterQuestionsSecond')
    var section3 = document.getElementById('lycterQuestionsThird')
    var LycterScales = [section1, section2, section3]

    var lucterScaleBackBtn = document.getElementById('lycher-scale-back')
    var lycterScaleNextBtn = document.getElementById('lycher-scale-next')
    var step_progress_target = document.getElementById('spender-profile-step-progress')
    var backButtonWithLink = document.getElementById('back-button-with-link')

    if(a.innerHTML === 'Next') {
        LycterScalesIndex += 1
        step_progress_target.innerHTML = LycterScalesIndex + 1
        for(let i = 0; i < LycterScales.length; i++) {
            var elm = LycterScales[i]
             elm.style.display = 'none'
        }
        document.getElementById(LycterScales[LycterScalesIndex].id).style.display = 'block'

    }

    if(a.innerHTML === 'Back') {
        LycterScalesIndex -= 1
        step_progress_target.innerHTML = LycterScalesIndex + 1
        for(let i = 0; i < LycterScales.length; i++) {
            var elm1 = LycterScales[i]
             elm1.style.display = 'none'
        }
        document.getElementById(LycterScales[LycterScalesIndex].id).style.display = 'block'
    }

    if(LycterScalesIndex === 0) {
        lucterScaleBackBtn.style.display = 'none'
        backButtonWithLink.style.display = 'flex'
    }
    if(LycterScalesIndex !== 0) {
        backButtonWithLink.style.display = 'none'
    }
    if(LycterScalesIndex === 1) {
        lucterScaleBackBtn.style.display = 'block'
    }
    if(LycterScalesIndex === 2) {
        lycterScaleNextBtn.style.display = 'none'
    } else {
        lycterScaleNextBtn.style.display = 'block'
    }



}