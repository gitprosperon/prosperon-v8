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