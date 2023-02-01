function toggleRental(title, address, rent, bed, bath, sqft, desc, init){
    var rentalCardTarget = document.getElementById('left-specific-apartment');
    var allRentalCardTarget = document.getElementById('all-rentals-card');
    var apartmentTitleTarget = document.getElementById('apartment-title');
    var apartmentAddressTarget = document.getElementById('apartment-address');
    var apartmentRentTarget = document.getElementById('apartment-monthly-rent');
    var apartmentBedroomTarget = document.getElementById('apartment-bedroom');
    var apartmentBathroomTarget = document.getElementById('apartment-bathroom');
    var apartmentSqftTarget = document.getElementById('apartment-sqft');
    var apartmentDescriptionTarget = document.getElementById('apartment-description');
    var effectMonthlyCostTarget = document.getElementById('effect-monthly-cost');
    var effectInitialCostTarget = document.getElementById('effect-initial-cost');

    apartmentTitleTarget.innerText = title
    apartmentAddressTarget.innerText = address
    apartmentRentTarget.innerText = rent
    apartmentBedroomTarget.innerText = bed
    apartmentBathroomTarget.innerText = bath
    apartmentSqftTarget.innerText = sqft
    apartmentDescriptionTarget.innerText = desc
    effectMonthlyCostTarget.innerText = rent
    effectInitialCostTarget.innerText = init

    if(allRentalCardTarget.style.display === 'block') {
        allRentalCardTarget.style.display = 'none'
        rentalCardTarget.style.display = 'block'
    } else {
        allRentalCardTarget.style.display = 'block'
        rentalCardTarget.style.display = 'none'

    }

}


function showCreditCard(title, apr, yearlyFee, atmFee, creditCardDescription, feature1, feature2, feature3, feature4, signupFee) {
    var creditCardPopup = document.getElementById('creditCardPopUp')
    var AllCardsTarget = document.getElementById('all-credit-card-wrapper')
    var apply_buttonTarget = document.getElementById('applyBtn')
    var backButton = document.getElementById('backBtn')

    backButton.style.opacity = '0%'
    apply_buttonTarget.style.display = 'block'
    AllCardsTarget.style.display = 'none'
    creditCardPopup.style.display = 'block'

    // handeling targets
    var creditNameTarget = document.getElementById('credit-card-name')
    var aprTarget = document.getElementById('apr')
    var yearlyFeeTarget = document.getElementById('yearlyFee')
    var atmFeeTarget = document.getElementById('atmFee')
    var creditCardDescriptionTarget = document.getElementById('creditCardDescription')
    var feature1Target = document.getElementById('feature1')
    var feature2Target = document.getElementById('feature2')
    var feature3Target = document.getElementById('feature3')
    var feature4Target = document.getElementById('feature4')
    var monthlyCostTarget = document.getElementById('effect-monthly-cost')
    var signupFeeTarget = document.getElementById('effect-initial-cost')

    var yearly = Number(yearlyFee)
    var montlyCost = yearly / 12

    creditNameTarget.innerText = title
    aprTarget.innerText = apr
    yearlyFeeTarget.innerText = yearlyFee
    atmFeeTarget.innerText = atmFee
    creditCardDescriptionTarget.innerText = creditCardDescription
    feature1Target.innerText = feature1
    feature2Target.innerText = feature2
    feature3Target.innerText = feature3
    feature4Target.innerText = feature4
    monthlyCostTarget.innerText = montlyCost
    signupFeeTarget.innerText = signupFee

}

function backToCards() {
    var creditCardPopup = document.getElementById('creditCardPopUp')
    var AllCardsTarget = document.getElementById('all-credit-card-wrapper')
    var backButton = document.getElementById('backBtn')

    backButton.style.opacity = '100%'


    AllCardsTarget.style.display = 'block'

    creditCardPopup.style.display = 'none'


}

function showBankAccount() {

}