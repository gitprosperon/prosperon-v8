var appliedList = [];



function changeJob(title, company, location, type, hours, salary, id, logo, requirements, qualifications, object) {
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

    var elements = document.getElementsByClassName('job-container')

    for(let i = 0; i < elements.length; i++) {
        elements[i].style.backgroundColor = 'white'
    }

    object.style.backgroundColor ='#E7F6FF'






}


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
    if(appliedList.length === 3) {
        console.log('equal to 5')
        var list = appliedList.toString()
        appliedTarget.setAttribute('value', list)

        alert.style.display = 'flex'
        getAJobContaonerTarget.style.display = 'none'
    }

}



