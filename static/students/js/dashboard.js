function showSimulate(){
var simulateBtnTarget = document.getElementById('simulateBtn')

    simulateBtnTarget.style.display = 'block'

}

function simulateRun() {
    var selectIndex = this.parentElement.children[0].options.selectedIndex
    var selectedData = this.parentElement.children[0].options[selectIndex].value
    location.replace("/university/simulate/" + selectedData)


}



var simulateBtnTarget = document.getElementById('simulateBtn')

simulateBtnTarget.addEventListener('click', simulateRun)


