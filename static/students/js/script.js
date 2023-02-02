


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


