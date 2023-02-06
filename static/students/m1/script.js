var appliedList = [];


// logic for changing job
function changeJob(title, company, location, type, hours, salary, id, logo, requirements, qualifications, description, object) {
    console.log('test')
    var jobTitleTarget = document.getElementById('job-title');
    var jobCompanyTarget = document.getElementById('job-company');
    var jobLocationTarget = document.getElementById('job-location');
    var jobTypeTarget = document.getElementById('job-type');
    var jobHoursTarget = document.getElementById("job-hours");
    var applyButton = document.getElementById('apply-to-job-button');
    var jobSalaryTarget = document.getElementById('salary-range');
    var imageTarget = document.getElementById('job-image')
    var jobRequirementsTarget = document.getElementById('job-requirmenets');
    var jobQualificationsTarget = document.getElementById('job-qualifications')
    var jobDescriptionTarget = document.getElementById('job-description')
    applyButton.setAttribute('value', id)

    if(appliedList.includes(id)) {
        applyButton.innerText = 'Applied';
        applyButton.style.backgroundColor = 'green'
    } else {
        applyButton.innerText = 'Apply';
        applyButton.style.backgroundColor = '#1f79ba'
    }

    jobTitleTarget.innerText = title;
    jobCompanyTarget.innerText = company;
    jobLocationTarget.innerHTML = location;
    jobTypeTarget.innerHTML = type;
    jobHoursTarget.innerHTML = hours;
    jobSalaryTarget.innerHTML = salary;
    imageTarget.src = '../../media/' + logo;
    jobRequirementsTarget.innerHTML = requirements;
    jobQualificationsTarget.innerHTML = qualifications;
    jobDescriptionTarget.innerHTML = description

    var elements = document.getElementsByClassName('job-container')

    for(let i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor = 'white'
    }
    object.style.backgroundColor ='#E7F6FF'

}


// function to change job to applied and add to list
function changeToApplied(a) {
    var button = document.getElementById('apply-to-job-button');
    var alert = document.getElementById('alert');
    var appliedTarget = document.getElementById('jobs-applied');
    var getAJobContaonerTarget = document.getElementById('get-a-job-container')
    if(appliedList.includes(button.value)) {
        console.log('yes')
    } else {
        appliedList.push(button.value);
        console.log('no')

    }
    button.innerText = 'Applied';
    button.style.backgroundColor = 'green';
    console.log('applied list', appliedList)
    if(appliedList.length === 5) {
        console.log('equal to 5')
        var list = appliedList.toString()
        appliedTarget.setAttribute('value', list)
        alert.style.display = 'flex'
        getAJobContaonerTarget.style.display = 'none'
    }

}


// toggle for job offer
function showJobOffer(companyName, companyLogo, jobLocation, jobType, jobHours, jobSalary, _401k, health, dental, vision, pto, studentLoans, relocation, firstName, lastName, payStructure, jobPosition) {
    var jobOfferTarget = document.getElementById('offerLetter')
    var offersTarget = document.getElementById('offers')
    jobOfferTarget.style.display = 'block'
    offersTarget.style.display = 'none'

    var companyNameTarget = document.getElementById('job-offer-companyName')
    var companyLogoTarget = document.getElementById('companyLogo')
    var jobSalaryTarget = document.getElementById('jobSalary')
    var _401kTarget = document.getElementById('401kWrapper')
    var healthTarget = document.getElementById('healthWrapper')
    var dentalTarget = document.getElementById('dentalWrapper')
    var visionTarget = document.getElementById('visionWrapper')
    var ptoTarget = document.getElementById('ptoWrapper')
    var studentLoanTarget = document.getElementById('studentLoanWrapper')
    var relocationTarget = document.getElementById('relocationWrapper')
    var nameTarget = document.getElementById('firstName')
    var lastNameTarget = document.getElementById('lastName')
    var companyTarget = document.getElementById('companyName-Offer')
    var companyTarget2 = document.getElementById('companyName2')
    var payStructureTarget = document.getElementById('payStructure')
    var jobStyleTarget = document.getElementById('workStyle')
    var jobHoursTarget = document.getElementById('jobHours')
    var jobHoursTarget2 = document.getElementById('jobHours2')
    var jobPositionTarget = document.getElementById('jobPosition')
    var jobPositionTarget2 = document.getElementById('jobPosition2')
    var jobPositionTarget3 = document.getElementById('jobPosition3')

    if(_401k === 'Yes') {
        _401kTarget.style.display = 'block'
    } else {
        _401kTarget.style.display = 'none'
    }

    if(health === 'Yes') {
        healthTarget.style.display = 'block'
    } else {
        healthTarget.style.display = 'none'
    }

    if(dental === 'Yes') {
        dentalTarget.style.display = 'block'
    } else {
        dentalTarget.style.display = 'none'
    }

    if(vision === 'Yes') {
        visionTarget.style.display = 'block'
    } else {
        visionTarget.style.display = 'none'
    }

    if(pto === 'Yes') {
        ptoTarget.style.display = 'block'
    } else {
        ptoTarget.style.display = 'none'
    }

    if(studentLoans === 'Yes') {
        studentLoanTarget.style.display = 'block'
    } else {
        studentLoanTarget.style.display = 'none'
    }

    if(relocation === 'Yes') {
        relocationTarget.style.display = 'block'
    } else {
        relocationTarget.style.display = 'none'
    }


    companyNameTarget.innerText = companyName
    companyLogoTarget.src = companyLogo
    jobSalaryTarget.innerText = jobSalary
    nameTarget.innerText = firstName
    lastNameTarget.innerText = lastName
    companyTarget.innerText = companyName
    companyTarget2.innerText = companyName
    payStructureTarget.innerText = payStructure
    jobStyleTarget.innerText = jobType
    jobHoursTarget.innerText = jobHours
    jobHoursTarget2.innerText = jobHours
    jobPositionTarget.innerText = jobPosition
    jobPositionTarget2.innerText = jobPosition
    jobPositionTarget3.innerText = jobPosition


}

function backToOffers() {
    var jobOfferTarget = document.getElementById('offerLetter')
    var offersTarget = document.getElementById('offers')

    jobOfferTarget.style.display = 'none'
    offersTarget.style.display = 'block'
}
